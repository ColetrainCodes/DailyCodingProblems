#Daily Coding Problems - Problem #1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import unittest

arrayOfNumbers = [10,15,3,7,9,12,27,38]

def pairOfNumbersAddToSum(Array, arraySize, sum):
	sortedArray = sorted(Array)
	leftIndex = 0
	rightIndex = arraySize - 1

	while leftIndex < rightIndex:
		if(Array[leftIndex] + Array[rightIndex] == sum):
			return 1
		elif(Array[leftIndex] + Array[rightIndex] < sum):
			leftIndex += 1
		else:
			rightIndex -= 1

	return 0

class unitTests(unittest.TestCase):
	def test1(self):
		self.assertTrue(pairOfNumbersAddToSum(arrayOfNumbers, len(arrayOfNumbers), 17))

	def test2(self):
		self.assertTrue(pairOfNumbersAddToSum(arrayOfNumbers, len(arrayOfNumbers), 22))

	def test3(self):
		self.assertFalse(pairOfNumbersAddToSum(arrayOfNumbers, len(arrayOfNumbers), 6))

	def test4(self):
		self.assertFalse(pairOfNumbersAddToSum(arrayOfNumbers, len(arrayOfNumbers), 100))


if __name__ == '__main__':
    unittest.main()