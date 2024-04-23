import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Search Engine", response.data)

    def test_handle_query(self):
        query_data = {'query': 'adventure', 'top_k': 3}
        response = self.app.post('/query', json=query_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('results', data)
        self.assertEqual(len(data['results']), 3)

    def test_handle_empty_query(self):
        query_data = {'query': ''}
        response = self.app.post('/query', json=query_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_handle_invalid_query(self):
        query_data = {}
        response = self.app.post('/query', json=query_data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
