import unittest
import caesar
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
  @patch("caesar.encrypt", side_effect = [
  caesar.encrypt("something", 3),
  caesar.encrypt("something", 7),
  caesar.encrypt("siphesihle", 5),
  caesar.encrypt("lwandile", 9),
  ])
  def test_encrypt(self, en):
    self.assertEqual(caesar.encrypt(), "vrphwklqj")
    self.assertEqual(caesar.encrypt(), "zvtlaopun")
    self.assertEqual(caesar.encrypt(), "xnumjxnmqj")
    self.assertEqual(caesar.encrypt(), "ufjwmrun")

  @patch("caesar.decrypt", side_effect = [
    caesar.decrypt("vrphwklqj", 3),
    caesar.decrypt("zvtlaopun", 7),
    caesar.decrypt("xnumjxnmqj", 5),
    caesar.decrypt("ufjwmrun", 9),
  ])
  def test_decrypt(self, en):
    self.assertEqual(caesar.decrypt(), "something")
    self.assertEqual(caesar.decrypt(), "something")
    self.assertEqual(caesar.decrypt(), "siphesihle")
    self.assertEqual(caesar.decrypt(), "lwandile")


if __name__ == "__main__":
  unittest.main()