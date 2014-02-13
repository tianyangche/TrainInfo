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

# Output the result in a human-friendly format
	print('Train Line' + '\t' + 'Route' + '\t\t' + 'Run Number' + '\t' + 'Operator ID')
	for i in range(0, len(temp)):
		print(temp[i][0] + '\t\t' + temp[i][1] + '\t' + temp[i][2] + '\t\t' + temp[i][3])
	f.close()
	return temp
