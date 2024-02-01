from typing import TYPE_CHECKING, Type
from typing import Any, Dict
from dotenv import load_dotenv
import os
import signal
import multiprocessing as mp
import time
from datetime import datetime
import shutil

if TYPE_CHECKING :
    from infrastructure.ftp.FTPservice import FTPservice
    from infrastructure.RCON.RCONservice import RCONservice
    from utils.CustomLogger import CustomLogger

t_ftp_service = Type["FTPservice"]
t_logger_service = Type["CustomLogger"]
t_rcon_service = Type["RCONservice"]

logger_message_queue: "mp.Queue[Dict[str, Any]]" = mp.Queue()
evt_logger: Any = mp.Event()

# UNIX USER
def manage_ctrl_c(*args: Any) -> None:
    """This methods is using to stop proccess correctly

    Args:
        *args (list): list of args

    Returns:
        None
    """

    # If you have multiple event processing processes, set each Event.
    print("\nStopping Service...\n")
    logger_message_queue.put(
        {
            "log": "app",
            "type": "INFO",
            "message": (
                "+++++++++++++++++ STOPPING APP FROM MAIN +++++++++++++++++"
            ),
        }
    )
    time.sleep(1)
    evt_logger.set()
    logger_message_queue.put(
        {
            "log": "app",
            "type": "INFO",
            "message": "+++++++++++++++++ APP STOPPED +++++++++++++++++",
        }
    )
    time.sleep(0.5)
    os.killpg(0, signal.SIGKILL)

def main(ftp_service: t_ftp_service, logger: t_logger_service, rcon_service: t_rcon_service) -> None:
    if not os.path.exists("./log/"):
        os.makedirs("./log")

    # Initialize the logger
    logger_message_queue: mp.Queue[Dict[str, Any]] = mp.Queue()
    debug_log_level = True
    evt_logger = mp.Event()
    custom_logger = mp.Process(
        target=logger.process,  # type: ignore
        args=(
            logger_message_queue,
            evt_logger,
            debug_log_level,
        ),
    )

    try:
        # signal.signal(signal.SIGINT, manage_ctrl_c)
        custom_logger.start()
        logger_message_queue.put(
            {"log": "app", "type": "INFO", "message": ">>> STARTING LOGGER <<<"}
        )
        #Chargement des données d'authentification
        load_dotenv()
        HOSTNAME = os.getenv("HOSTNAME")
        USERNAME = os.getenv("USERNAME_SERVER")
        PWD = os.getenv("PWD")
        REMOTE_PATH = os.getenv("REMOTE_PATH")
        LOCAL_DIR = os.getenv("LOCAL_PATH")
        SAVE_DIR = LOCAL_DIR + "\\Saves"
        RCON_PWD = os.getenv("RCON_PWD")
        
        #Initialiser l'objet FTP
        saver = ftp_service(HOSTNAME, USERNAME, PWD)
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": "FTP service init succeed",
                }
            )

        #Connection au serveur en FTP
        saver.connect()
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": "Connected to FTP with success",
                }
            )

        #Check du nombre de save : si > 5 on supprime le plus ancien
        os.makedirs(SAVE_DIR, exist_ok=True)
        listing_dir = os.listdir(SAVE_DIR)
        listing_dir.sort(reverse=True)
        if len(listing_dir) >= 5:
            shutil.rmtree(SAVE_DIR + "\\" + listing_dir[-1], ignore_errors=True)
            logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": f" Folder {SAVE_DIR}/{listing_dir[-1]} removed with success",
                }
            )
        
        #Création du répertoire du jour
        now = datetime.now()
        NEW_DIR = now.strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs(SAVE_DIR + "/" + NEW_DIR)
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": f" Data will be saved in : {SAVE_DIR}/{NEW_DIR}",
                }
            )

        #Téléchargement des datas dans le répertoire du jour
        saver.download_all_files_recursive(REMOTE_PATH, SAVE_DIR + "/" + NEW_DIR)
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": f" All data downloaded with success in :  {SAVE_DIR}/{NEW_DIR}",
                }
            )
        
        #Connexion au serveur en RCON
        rcon = rcon_service(HOSTNAME, RCON_PWD)
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": "RCON service init succeed",
                }
            )
        rcon.connect()
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": "Successfully contacted RCON server",
                }
            )

        #Déconnexion du serveur
        saver.disconnect()
        logger_message_queue.put(
                {
                    "log": "app",
                    "type": "INFO",
                    "message": "Disconnected from server successfully",
                }
            )
    
    except Exception as e:
        logger_message_queue.put(
            {
                "log": "app",
                "type": "ERROR",
                "message": (
                    "An error occured : >>>>>>>>  Please check the"
                    " error logs.  <<<<<<<<"
                ),
            }
        )
        logger_message_queue.put(
            {
                "log": "error",
                "type": "ERROR",
                "message": (e),
            }
        )
        raise e

    finally:
        logger_message_queue.put(
            {
                "log": "app",
                "type": "INFO",
                "message": ">>> STOPPING APP <<<",
            }
        )
        time.sleep(0.1)
        evt_logger.set()