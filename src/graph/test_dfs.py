from unittest import TestCase
from dfs import *
from graph import *

class TestDFS(TestCase):

	def setUp(self):
		self.g1 = Graph()
		self.g1.add_edge('s', 'p')
		self.g1.add_edge('s', 'e')
		self.g1.add_edge('s', 'd')
		self.g1.add_edge('b', 'a')
		self.g1.add_edge('d', 'e')
		self.g1.add_edge('d', 'c')
		self.g1.add_edge('d', 'b')
		self.g1.add_edge('p', 'q')
		self.g1.add_edge('c', 'a')
		self.g1.add_edge('h', 'q')
		self.g1.add_edge('h', 'p')
		self.g1.add_edge('e', 'r')
		self.g1.add_edge('e', 'h')
		self.g1.add_edge('r', 'f')
		self.g1.add_edge('f', 'g')
		self.g1.add_edge('f', 'c')

		self.g2 = Graph()
		self.g2.add_edge('s', 'd')
		self.g2.add_edge('d', 'e')
		self.g2.add_edge('e', 's')
		self.g2.add_edge('e', 'g')


	def test_path_source_dont_exist(self):
		path = []
		self.assertRaises(VerticeNotFoundException, dfs, 'z', 'g', self.g1)

	def test_path_target_not_found1(self):
		path = []
		self.assertEqual(dfs('s', 'z', self.g1), None)

	def test_path_found1(self):
		path = ['s', 'e', 'r', 'f', 'g']
		self.assertEqual(dfs('s', 'g', self.g1), path)

	def test_path_found2(self):
		path = ['s', 'e', 'h', 'q']
		self.assertEqual(dfs('s', 'q', self.g1), path)

	def test_path_infinite_loop(self):
		path = ['s', 'd', 'e', 'g']
		self.assertEqual(dfs('s', 'g', self.g2), path)