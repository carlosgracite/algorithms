from unittest import TestCase
from dfs import *
from util import build_path

class TestDFS(TestCase):

	def setUp(self):
		self.g1 = Graph()
		g1.add_edge('s', 'p')
		g1.add_edge('s', 'e')
		g1.add_edge('s', 'd')
		g1.add_edge('b', 'a')
		g1.add_edge('d', 'e')
		g1.add_edge('d', 'c')
		g1.add_edge('d', 'b')
		g1.add_edge('p', 'q')
		g1.add_edge('c', 'a')
		g1.add_edge('h', 'q')
		g1.add_edge('h', 'p')
		g1.add_edge('e', 'r')
		g1.add_edge('e', 'h')
		g1.add_edge('r', 'f')
		g1.add_edge('f', 'g')
		g1.add_edge('f', 'c')

		self.g2 = Graph()
		g2.add_edge('s', 'd')
		g2.add_edge('d', 'e')
		g2.add_edge('e', 's')
		g2.add_edge('e', 'g')


	def test_path_source_dont_exist(self):
		path = []
		self.assertRaises(VerticeNotFoundException, dfs, 'z', 'g', self.g1)

	def test_path_target_not_found1(self):
		path = []
		self.assertEqual(build_path(dfs('s', 'z', self.g1), 'z'), path)

	def test_path_found1(self):
		path = ['s', 'e', 'r', 'f', 'g']
		self.assertEqual(build_path(dfs('s', 'g', self.g1), 'g'), path)

	def test_path_infinite_loop(self):
		path = []
		self.assertEqual(build_path(dfs('s', 'g', self.g2), 'g'), path)