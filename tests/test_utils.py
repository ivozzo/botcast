import app.Bot.utils as utils
from app.Bot.action import Action


class TestUtils:

    def test_convert_actions(self):
        test_actions = [{'chat_message': ['Gimme an A', 'Gimme a B', 'Gimme a C', 'ABC!']}]
        converted_action = utils.convert_actions(test_actions)

        assert len(converted_action) == 1

        for action in converted_action:
            assert type(action) is Action

        action = converted_action[0]
        assert action.type == "chat_message"
        assert len(action.messages) == 4
        assert action.messages[0] == 'Gimme an A'
        assert action.messages[2] == 'Gimme a C'
