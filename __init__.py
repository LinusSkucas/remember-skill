from mycroft import MycroftSkill, intent_handler, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger

__author__ = "Linus S (LinusS1/brrn)"

LOGGER = getLogger(__name__)

class RememberSkill(MycroftSkill):
    def __init__(self):
        super(RememberSkill, self).__init__(name='RememberSkill')

    @intent_file_handler("remember.intent")
    def handle_remember_that(self, message):
        thought = "that " + message.data.get("thought")
        self.settings["thought"] = str(thought)
        self.speak_dialog("remember")

    @intent_file_handler("recall.intent")
    def handle_recall(self, message):
        thought = self.settings.get("thought")
        self.speak_dialog("recall", data={"thought": thought})

def create_skill():
    return RememberSkill()

