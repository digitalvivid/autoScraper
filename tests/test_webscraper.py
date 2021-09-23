import unittest
from webscraper.webscraper import scrape
from webscraper.webscraper import result

class WebScraperTests(unittest.TestCase):
    def test_function(self):
        result()
        self.assertEqual(result(), True)

class WebScraperTests(unittest.TestCase):
    def test_function(self):
        scrape()
        self.assertEqual(scrape(), True)
    

# if we run module directly, run code in this conditional
if __name__ == "__main__":
    unittest.main()
