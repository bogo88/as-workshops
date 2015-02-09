import app
import unittest


class TestList(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_list(self):
        resp = self.app.get('/absence')
        self.assertEqual('Absence list', resp.data)


class TestDetail(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_detail(self):
        resp = self.app.get('/absence/1')
        self.assertEqual('Absence detail 1', resp.data)


class TestCreate(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_create(self):
        resp = self.app.post('/absence')
        self.assertEqual('Absence create', resp.data)


class TestEdit(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_edit(self):
        resp = self.app.put('/absence/1')
        self.assertEqual('Absence edit 1', resp.data)


class TestDelete(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_delete(self):
        resp = self.app.delete('/absence/1')
        self.assertEqual('Absence delete 1', resp.data)

if __name__ == '__main__':
    unittest.main()