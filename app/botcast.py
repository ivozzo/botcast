import sys
import getopt
from Logger.logger import Logger
from Configuration.configuration import Configuration
from Owncast.client import Client

log_level = 'INFO'
settings = './settings.yml'


def main(argv):
    global log_level, settings
    opts, args = getopt.getopt(argv, "hl:s:", ["level=", "settings="])
    for opt, arg in opts:
        if opt == '-h':
            print('botcast.py -s <settings file [path]> -l <log level [INFO, DEBUG, WARN, ERROR]>')
            sys.exit()
        elif opt in ("-l", "--level"):
            log_level = arg
        elif opt in ("-s", "--settings"):
            settings = arg


if __name__ == "__main__":
    main(sys.argv[1:])

logger = Logger(log_level)

logger.info(f'Bostcast starting')

# Configuration
logger.info('Reading configuration file')
configuration = Configuration(path='./', filename='test.yml').loaded

if logger.is_debug():
    for doc, items in configuration.items():
        if doc != 'owncast':
            logger.debug(f'{doc}, {items}')

# Establishing connection
url = configuration['owncast']['url']
logger.info(f'Establishing connection with {url}')
owncast = Client(url=url)

logger.info(owncast)
