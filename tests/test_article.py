import unittest

class ArticleTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the class
  '''

  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_article = Article('Jeremy', 'Jeremy', 'Jeremy', 'Jeremy', 'Jeremy') 

  def test_init(self):
    self.assertTrue(isinstance(self.new_article, Article))

if __name__ == '__main__':
  unittest.main()