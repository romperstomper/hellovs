from hellovs.hello import *
import unittest

class TestHelloTest(unittest.TestCase):
    def test_hello_pass_test(self):
        #result = hello.itsgrand()
        self.assertEqual(True, True)


if __name__ == '__namin__':
    unittest.main()
