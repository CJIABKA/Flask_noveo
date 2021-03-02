from abc import ABC, abstractmethod


class MessageTarget(ABC):

    def __init__(self, params, message):
        self.params = params
        self.message = message

    def process_message(self):
        self.get_params_and_message()
        if not self.validate():
            self.send_message()
            return None
        return self.validate()

    @abstractmethod
    def process_params_and_message(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def send_message(self):
        pass


class HTMLTarget(MessageTarget):

    def process_params_and_message(self):
        pass

    def validate(self):
        pass

    def send_message(self):
        pass


class SMSTarget(MessageTarget):

    def process_params_and_message(self):
        pass

    def validate(self):
        pass

    def send_message(self):
        pass
