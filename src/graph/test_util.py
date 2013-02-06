from unittest import TestCase
from util import *

class TestUtil(TestCase):

	def test_null_tree(self):
		self.assertEqual(build_path(None, None), [])

	def test_empty_tree(self):
		self.assertEqual(build_path({}, None), [])

	def test_one_vertice_found(self):
		self.assertEqual(build_path({'a':None}, 'a'), ['a'])

	def test_one_vertice_not_found(self):
		self.assertEqual(build_path({'b':None}, 'a'), [])

	def test_found1(self):
		tree = {'a':None, 'b':'a', 'c':'b', 'z':None}
		self.assertEqual(build_path(tree, 'c'), ['a', 'b', 'c'])

	def test_found2(self):
		tree = {'a':None, 'b':'a', 'c':'b', 'z':None}
		self.assertEqual(build_path(tree, 'z'), ['z'])

	def test_not_found(self):
		tree = {'a':None, 'b':'a', 'c':'b', 'z':None}
		self.assertEqual(build_path(tree, 'y'), [])
