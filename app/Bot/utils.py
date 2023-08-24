import logging
from .action import Action

logger = logging.getLogger()


def convert_actions(actions):
    for action in actions:
        if logger.level == logging.DEBUG:
            logger.debug(f'- converting action: {action}')

        actions_list = []

        if list(action.values())[0] is not None:
            actions_list.append(Action(command_type=list(action)[0], messages=list(action.values())[0]))

        for item in actions_list:
            logger.info(item.type)
            for message in item.messages:
                logger.info(message)

        return actions_list
