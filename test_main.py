import unittest
import main
from main import home_page

class TestMain(unittest.TestCase):

    # Assert status code 200 for both routes
    def test_home_page(self):
        tester = main.app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
                 
if __name__ == "__main__":
    unittest.main()       