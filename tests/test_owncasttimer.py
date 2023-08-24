from app.Bot.owncasttimer import OwncastTimer
from app.Bot.action import Action
import app.Bot.owncasttimer as timers

test_alias = 'ABC'
test_description = 'Test'
test_action_type = 'chat_message'
test_action_message = 'Eyo'
test_interval = '1'


class TestOwncasttimer:

    def test_creation(self):

        test_timer = {'alias': f'{test_alias}',
                      'description': f'{test_description}',
                      'actions': [
                          {f'{test_action_type}': [f'{test_action_message}']}
                      ],
                      'interval': f'{test_interval}'}

        timer = timers.create_timer(test_timer)

        assert timer is not None
        assert type(timer) is OwncastTimer
        assert timer.get_alias() == test_alias
        assert timer.get_description() == test_description
        assert timer.get_actions() is not None
        assert len(timer.get_actions()) == 1
        action = timer.get_actions()[0]
        assert type(action) is Action
        assert action.type == test_action_type
        assert len(action.messages) == 1
        assert action.messages[0] == test_action_message
