from mycroft import MycroftSkill, intent_file_handler


class Remember(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('remember.intent')
    def handle_remember(self, message):
        self.speak_dialog('remember')


def create_skill():
    return Remember()

