# from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
# from pynput.mouse import Controller


# mouse = Controller()


class InputControl(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    # @intent_file_handler('control.input.intent')
    # def handle_control_input(self, message):
    #     self.speak_dialog('control.input')
    #     self.speak('Yo man')
    #     self.speak(message)

    @intent_handler(IntentBuilder("ScrollIntent").require("scroll").require("down"))
    def handle_scrolldown_intent(self, message):
        print('scroll down')
        self.speak('scroll down yo')
        # mouse.scroll(0, -2)

    # @intent_handler(IntentBuilder("ScrollIntent").require("scroll").require("up"))
    # def handle_scrollup_intent(self, message):
    #     print('scroll up')
    #     mouse.scroll(0, 2)


def create_skill():
    return InputControl()

