
class Agent:
    def __init__(self):
        pass


class Template:
    def __init__(self):
        pass


class Message:
    def __init__(self, sender: str, recievers: list, message: str) -> None:
        self.sender = sender
        self.recievers = recievers
        self.message = message

