import unittest
from main import just_some_addition


class MyTestCase(unittest.TestCase):
  def test_main(self):
    self.assertEqual(just_some_addition(3, 3), 6)  # add assertion here

  def test_main_raises_exception(self):
    with self.assertRaises(Exception):
      just_some_addition(1, '2')

if __name__ == '__main__':
  unittest.main()
