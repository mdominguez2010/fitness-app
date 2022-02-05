import unittest
import main

class TestMain(unittest.TestCase):
    
    # Assert status code 200 for both routes
    def test_home_page(self):
        tester = main.home_page(self)
        
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Status code should be 200")
        self.assertTrue(b"Home" in response.data)
        
        response = tester.get("/home", content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Status code should be 200")
        self.assertTrue(b"Home" in response.data)
        
    # Test weight page
    def test_weight_page(self):
        tester = main.home_page(self)
        
        response = tester.get("/weight", content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Status code should be 200")
        self.assertTrue(b"TEST_WEIGHT_PAGE" in response.data)
    
    # Test strength page    
    def test_strength_page(self):
        tester = main.home_page(self)
        
        response = tester.get("/strength", content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Status code should be 200")
        self.assertTrue(b"TEST_STRENGTH_PAGE" in response.data)
    
    # Test cardio page    
    def test_cardio_page(self):
        tester = main.home_page(self)
        
        response = tester.get("/cardio", content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Status code should be 200")
        self.assertTrue(b"TEST_CARDIO_PAGE" in response.data)
        
if __name__ == "__main__":
    unittest.main()       