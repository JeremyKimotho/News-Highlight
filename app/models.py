class Source:
  '''
  This class is for the source object
  '''

  def __init__(self, name):
    self.name = name

  

class Article:
  '''
  This class defines the Article objects
  '''

  def __init__(self, author, headline, link_to_site, image, date_written):
    self.author = author
    self.headline = headline
    self.link_to_site = link_to_site
    self.image = image
    self.date_written = date_written

