import unittest
import json

def printboard(board):
	for i in range(8):
		for j in range(8):
			print board[i][j],
		print

def isSafe(board, row, col):
	for i in range(8):
		if board[row][i]==1:
			return False
	for i in range(8):
		for j in range(8):
			if board[i][j]==1:
				if abs(col-j)==abs(row-i):
					return False
	return True




def queenplace(board, col):
	if col>=8:
		printboard(board)
		print
		return True
	for i in range(8):
			if isSafe(board, i, col):
				board[i][col]=1
				queenplace(board, col+1)
				board[i][col]=0



def solve(filename):
	board=[[0 for i in range(8)] for i in range(8)]
	data=[]
	with open(filename, 'r') as f:
		data=json.load(f)
	if data["start"]>7 or data["start"]<1:
		print "Invalid data"
		exit()
	board[data["start"]][0]=1
	if queenplace(board, 1)==False:
			print "No sol"
			return False
	return True

	

class MyTest(unittest.TestCase):
	def test_positive(self):
		self.assertEqual(solve('input1.json'), True)
	def test_naegative(self):
		self.assertEqual(solve('input2.json'), False)



filename=raw_input("enter filename")
solve(filename)
print "----TestCases------"
unittest.main()
