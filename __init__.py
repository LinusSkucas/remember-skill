from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder

class RememberSkill(MycroftSkill):
    def __init__(self):
        super(RememberSkill, self).__init__(name='RememberSkill')

    @intent_handler(IntentBuilder("RememberIntent").require("remember").require("thought"))
    def handle_remember(self, message):
        thought = message.data.get("thought")
        self.settings["thought"] = str(thought)
        self.speak_dialog("remember")

    @intent_handler(IntentBuilder("RememberIntent").require("recall"))
    def handle_recall(self, message):
        thought = self.settings.get("thought")
        self.speak_dialog("recall", data={"thought" : str(thought)})

def create_skill():
    return RememberSkill()

