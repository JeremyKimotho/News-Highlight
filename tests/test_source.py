import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the article class
  '''

  def setUp(self):
    '''
    Set up method that will run before any test
    '''
    self.new_source = Source('Jeremy')

  def test_init(self):
    self.assertTrue(isinstance(self.new_source, Source))

if __name__ == '__main__':
  unittest.main()