import unittest
from src.todo_list import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.tdlist = TodoList([])
        self.tdlist2 = TodoList(["AA","BB"])

    def test_string_represting(self):
        self.assertEqual(str(self.tdlist), "All tasks:[], completed: set(), active: set().")

    def tearDown(self):
        pass