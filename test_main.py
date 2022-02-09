import unittest
import main


class TestMain(unittest.TestCase):

    # Assert status code 200 for both routes
    def test_home_page(self):
        tester = main.app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)

        response = tester.get("/home", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_weight_page(self):
        tester = main.app.test_client(self)
        response = tester.get("/weight", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_strength_page(self):
        tester = main.app.test_client(self)
        response = tester.get("/strength", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_cardio_page(self):
        tester = main.app.test_client(self)
        response = tester.get("/strength", content_type="html/text")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
