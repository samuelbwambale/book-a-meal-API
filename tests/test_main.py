import unittest
from main import hello_andela
from main import challange
from main import myFunction


class MainTest(unittest.TestCase):
    def test_hello_andela(self):
        self.assertEqual(hello_andela(), "Helloworld")


    def test_assertions(self):
        self.assertTrue("andela".islower)
        self.assertTrue("foo".upper, "FOO")

    def test_challange(self,value=10):
        self.assertEqual(type(challange(10),list))
        self.assertEqual(isinstance(challange(10),list))
        self.assertEqual(type(challange(10)[-1]), int)





if __name__ == "__main__":
    unittest.main()

