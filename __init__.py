# from mycroft import MycroftSkill, intent_file_handler
from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController


mouse = MouseController()
keyboard = KeyboardController()


class InputControl(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("ScrollDownIntent").require("scroll").require("down"))
    def handle_scrolldown_intent(self, message):
        mouse.scroll(0, -2)

    @intent_handler(IntentBuilder("ScrollUpIntent").require("scroll").require("up"))
    def handle_scrollup_intent(self, message):
        mouse.scroll(0, 2)

    @intent_handler(IntentBuilder("PageDownIntent").require("page").require("down"))
    def handle_pagedown_intent(self, message):
        keyboard.press(Key.page_down)

    @intent_handler(IntentBuilder("PageUpIntent").require("page").require("up"))
    def handle_pageup_intent(self, message):
        keyboard.press(Key.page_up)


def create_skill():
    return InputControl()

