import logging
from threading import Timer
from .utils import convert_actions

logger = logging.getLogger()


def timed_action(*args, **kwargs):
    logger.info(f'Executing timer {args[0]}')

    for action in args[2]:
        logger.info(action.messages)


class OwncastTimer(Timer):
    def run(self):
        logger.info(f'Activating timer {self.get_alias()}')
        while not self.finished.wait(int(self.interval)):
            self.function(*self.args, **self.kwargs)

    def get_alias(self):
        return self.args[0]

    def get_description(self):
        return self.args[1]

    def get_actions(self):
        return self.args[2]


def create_timer(timer):
    return OwncastTimer(interval=timer['interval'],
                        function=timed_action,
                        args=(timer['alias'], timer['description'], convert_actions(timer['actions'])))
