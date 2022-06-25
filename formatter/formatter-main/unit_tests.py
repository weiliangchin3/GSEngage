import unittest
import app

class ApiTest(unittest.TestCase):
    def test_invalid_body(self):
        j = {
            "body" : {}
        }
        self.assertEqual(False, app.isInvalidBody(j))
        

if __name__ == "__main__":
    unittest.main()