from rcon.source import Client
import multiprocessing as mp

class RCONservice:

    def __init__(self, hostname: str, pwd: str, port: int, logger_message_queue:mp.Queue) -> None:
        self.hostname = hostname
        self.pwd = pwd
        self.port = port
        self.logger_message_queue = logger_message_queue
        self.rcon = None

    def connect(self):
        print(f'Trying to notify server')
        try :
            with Client(self.hostname, self.port, passwd=self.pwd) as client:
                client.run('Broadcast','Save_Done')
        except Exception as e:
            self.logger_message_queue.put(
                {
                    "log": "error",
                    "type": "ERROR",
                    "message": "Error while connecting to RCON server :" + str(e),
                }
            )
            pass
