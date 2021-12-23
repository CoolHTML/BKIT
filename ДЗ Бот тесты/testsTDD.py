import unittest
import telebot
from main import send_number
from main import send_number
bot = telebot.TeleBot('1950557144:AAGkgcjdtkmmyT3p43izeRNwDtsZgU2Y1P8')
class Test_bott(unittest.TestCase):
    def test_1(self):
        self.assertEqual(send_number(), 4)
    def test_2(self):
        self.assertEqual(send_number(),17)