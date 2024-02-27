import unittest
from telebot.types import Message

from bot import start

class TestHandlers(unittest.TestCase):

    def test_start_message_handler_initial(self):
        message = Message()
        message.chat.id = 123456789
        start(message)


    def test_start_message_handler_final(self):
        message = Message()
        message.chat.id = 987654321

        start(message)
      
unittest.main()