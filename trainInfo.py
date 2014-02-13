#!/usr/bin/python
import csv
def trainInfoFunc( ):
# open file from user input
	x = raw_input("Enter name of the csv file:")
	f = open('test1.csv', 'rb')
	reader = csv.reader(f)
	result = []
# read data, store it into a list, then sort it
	for line in reader:
		result.append(line)
	result = result[1:]
	temp = sorted(result, key=lambda result: result[2])
	f.close()
	return temp

def printFunc(result):
        print('Train Line' + '\t' + 'Route' + '\t\t' + 'Run Number' + '\t' + 'Operator ID')
# Output the result in a human-friendly format
        for i in range(0, len(result)):
                print(result[i][0] + '\t\t' + result[i][1] + '\t' + result[i][2] + '\t\t' + result[i][3])


if __name__ == '__main__':
	finalResult = trainInfoFunc()
	printFunc(finalResult)	
