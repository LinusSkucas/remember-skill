from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger

__author__ = "LinusS1"

LOGGER = getLogger(__name__)

class RememberSkill(MycroftSkill):
    def __init__(self):
        super(RememberSkill, self).__init__(name='RememberSkill')

    @intent_handler(IntentBuilder("RememberIntent").require("remember").optionally("thought"))
    def handle_remember(self, message):
        thought = message.data.get("thought")
        if "what" in message.data["utterance"]:
            thought = self.settings.get("thought")
            self.speak_dialog("recall", data={"thought" : thought})
        else:
            self.settings["thought"] = str(thought)
            self.speak_dialog("remember")

def create_skill():
    return RememberSkill()

