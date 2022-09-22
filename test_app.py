import unittest
import requests


class TestApp(unittest.TestCase):
    test_url = "http://127.0.0.1:5000/books"

    def test_check_code(self):

        response = requests.get(self.test_url)
        self.assertEqual(response.status_code, 200)

    def test_check_book(self):
        response = requests.get(self.test_url)
        json_response = response.json()
        self.assertEqual(json_response['id'], 1)


if __name__ == '__main__':
    unittest.main()

