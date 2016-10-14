#!/usr/bin/env python3
import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_mult(self):
		result = rpn.calculate("4 0 *")
		self.assertEqual(0, result)
	def test_div(self):
		result = rpn.calculate("10 5 /")
		self.assertEqual(2, result)
	def test_exp(self):
		result = rpn.calculate("2 5 ^")
		self.assertEqual(32, result)
	def test_mod(self):
		result = rpn.calculate("9 4 %")
		self.assertEqual(1, result)
	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
