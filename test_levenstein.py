import csv
import pytest
from levenshtein import levenshtein_distance


def test_same_word():
	assert levenshtein_distance("this", "this") == 0

def test_w1_shorter_than_w2():
	assert levenshtein_distance("the", "that is correct") == 13

def test_w1_larger_than_w2():
	assert levenshtein_distance("that is correct", "the") == 13

def test_w1_larger_than_w2_v2():
	assert levenshtein_distance("the", "that") == 2

def test_same_length():
	assert levenshtein_distance("this", "that") == 2

def test_examples():
	with open('data/examples.csv', newline='') as csvfile:
		examples = csv.reader(csvfile)
		for row in examples:
			assert levenshtein_distance(row[0], row[1]) == int(row[2])