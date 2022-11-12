import unittest
import caesar

class MyTestCase(unittest.TestCase):
  def test_get_input():
    user_input = caesar.get_user_input