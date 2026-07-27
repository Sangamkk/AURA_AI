import json
import os


class MemoryManager:

    def __init__(self):
        self.history_folder = "data/history"
        os.makedirs(
            self.history_folder,
            exist_ok=True
        )

    def save_chat(self,filename,messages):
        path = os.path.join(
            self.history_folder,
            filename
        )
        with open(path,"w",encoding="utf-8") as file:
            json.dump(
                messages,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_chat(self, filename):
        path = os.path.join(self.history_folder,filename)
        if not os.path.exists(path):
            return []
        with open(path,"r",encoding="utf-8") as file:
            return json.load(file)

    def list_chats(self):
        return os.listdir(
            self.history_folder
        )

    def delete_chat(self, filename):
        path = os.path.join(
            self.history_folder,
            filename
        )
        if os.path.exists(path):
            os.remove(path)
            
    def create_new_chat(self):
        chats = self.list_chats()
        number = len(chats) + 1
        filename = f"Chat_{number}.json"
        self.save_chat(filename, [])
        return filename        