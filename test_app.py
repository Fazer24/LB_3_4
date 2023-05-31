import unittest
from app import app, find_roots

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Коэффициент a:', response.data.decode('utf-8'))

    def test_find_roots(self):
        # Тестирование нахождения корней
        root1, root2 = find_roots(1, -3, 2)
        self.assertEqual(root1, 2.0)
        self.assertEqual(root2, 1.0)

        # Тестирование единственного корня
        root, _ = find_roots(1, -2, 1)
        self.assertEqual(root, 1.0)

        # Тестирование отсутствия корней
        roots = find_roots(1, 2, 3)
        self.assertIsNone(roots[0]) 
        self.assertIsNone(roots[1]) 

    def test_submit_form(self):
        response = self.client.post('/', data={
            'coefficient_a': '1',
            'coefficient_b': '-3',
            'coefficient_c': '2'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Единственный корень: 2.0', response.data.decode('utf-8'))
        self.assertIn('Корень 2: 1.0', response.data.decode('utf-8'))

        response = self.client.post('/', data={
            'coefficient_a': '1',
            'coefficient_b': '-2',
            'coefficient_c': '1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Единственный корень: 1.0', response.data.decode('utf-8'))

        response = self.client.post('/', data={
            'coefficient_a': '1',
            'coefficient_b': '2',
            'coefficient_c': '3'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Корни отсутствуют', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
