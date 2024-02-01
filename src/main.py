# Modules
import sys

# TOOLS
# FTP
from infrastructure.ftp.FTPservice import FTPservice
# RCON
from infrastructure.RCON.RCONservice import RCONservice

# LOGGER
from utils.CustomLogger import CustomLogger

# Import app
from app.core import main

if __name__ == "__main__":
    try:
        main(ftp_service=FTPservice, logger=CustomLogger,rcon_service=RCONservice)
        sys.exit()
    except Exception as e:
        print(f"An error occured, please check the logs.\n{e}")
        sys.exit()