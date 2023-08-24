import sys
import getopt
from Logger.logger import Logger
from Configuration.configuration import Configuration
import Bot.owncasttimer as timer

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

'''
CONFIGURATION

This snippet reads the configuration file
'''
logger.info('Reading configuration file')
try:
    configuration = Configuration(settings).loaded
except FileNotFoundError:
    logger.error(f'Error while reading file {settings}, check out file existence, file permissions and file syntax')
    sys.exit(1)

if logger.is_debug():
    for doc, items in configuration.items():
        if doc != 'owncast':
            logger.debug(f'{doc}, {items}')

logger.info('#################')
logger.info('# CONFIGURATION #')
logger.info('#################')

'''
TIMERS

This snippet checks if there are any timers loaded from the configuration
and start them as a wrapped threading.Timer class 
'''
if configuration['timers'] is None:
    logger.info('No timers found in the configuration, moving on')
else:
    timers_number = len(configuration['timers'])
    logger.info(f'Creating timers, found {timers_number} elements')
    timers = []
    for item in configuration['timers']:
        logger.info(f'- processing {item["alias"]}')

        timers.append(timer.create_timer(item))

        for timer in timers:
            logger.info(timer.interval)
            timer.start()


'''
COMMANDS

This snippet will definitely do something in the near future, I promise
'''
if configuration['commands'] is None:
    logger.info('No timers found in the configuration, moving on')

logger.info(f'Bostcast started')
