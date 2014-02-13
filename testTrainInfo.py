import unittest
from trainInfo import trainInfoFunc
def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
	result = trainInfoFunc()
	for i in range(0, len(result)-1):
		self.assertLessEqual(result[i][2], result[i+1][2])
		
if __name__ == '__main__':
    unittest.main()
