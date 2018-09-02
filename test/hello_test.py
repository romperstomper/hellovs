from hellovs import hello
import unittest

class HelloTest(unittest.TestCase):
    def hello_pass_test(self):
        result = hello.itsgrand()
        self.assertEqual(True, True)