# coding: utf-8

import unittest
import bellman_ford
import random

class TestBellmanFord(unittest.TestCase):

    def test_bellman_ford_1(self):
        graph = [
            #s,   1, 2,  3,  4, t
            [0,   6, 8, 18,  0, 0], #s
            [6,   0, 0,  0, 11, 0], #1
            [8,   0, 0,  9,  0, 7], #2
            [18,  0, 9,  0,  0, 4], #3
            [0,  11, 0,  0,  0, 3], #4
            [0,   0, 7,  4,  3, 0], #t
        ]
        exp = [0, 2, 5]
        start = 0
        goal = 5
        self.assertEqual(bellman_ford.bellman_ford(graph, start, goal), exp)

    def test_bellman_ford_2(self):
        graph = [
            #s, 1, 2, 3, 4, t
            [0, 5, 4, 2, 0, 0], #s
            [5, 0, 2, 0, 0, 6], #1
            [4, 2, 0, 3, 2, 0], #2
            [2, 0, 3, 0, 6, 0], #3
            [0, 0, 2, 6, 0, 4], #4
            [0, 6, 0, 0, 4, 0], #t
        ]
        exp = [0, 2, 4, 5]
        start = 0
        goal = 5
        self.assertEqual(bellman_ford.bellman_ford(graph, start, goal), exp)
