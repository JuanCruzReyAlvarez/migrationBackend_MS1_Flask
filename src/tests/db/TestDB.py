
from src.resource.db.DB import DB
import unittest

class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = DB()
    
    def test_getURI(self):
        assert self.db.getURI() is not None

    def test_connect(self):
        assert self.db.connect is not None



