class ConversationMemory:

    def __init__(self):

        self.messages = []

    def add_user_message(self, text):

        self.messages.append({
            "role": "user",
            "text": text
        })

    def add_ai_message(self, text):

        self.messages.append({
            "role": "assistant",
            "text": text
        })

    def get_history(self):

        return self.messages

    def clear(self):

        self.messages.clear()