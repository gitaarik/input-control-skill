from mycroft import MycroftSkill, intent_file_handler


class InputControl(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.input.intent')
    def handle_control_input(self, message):
        self.speak_dialog('control.input')


def create_skill():
    return InputControl()

