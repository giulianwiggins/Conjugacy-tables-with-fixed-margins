#!/usr/bin/env python3
import numpy as np
					
def topRow(rowsum, columns): #rowsum is an integer, columns is an array of integers
	# This generator yields all the possible top rows of a matrix with first row summing to the integer rowsum, and j-th column summing to columns[j]
	if len(columns) == 1:
		yield [min(rowsum, columns[0])] 
	else:
		for i in range(max(rowsum - sum(columns[1:]),0), min(rowsum, columns[0]) + 1): # For i to be in position [0,0] we must have: sum(columns[1:]) + i >= rowsum
			for row in topRow(rowsum - i, columns[1:]):
				yield [i] + row
					

def arrays(rows, columns):
	# This generator returns all 2D arrays of integers in which the i-th row sums to rows[i] and the j-th column sums to columns[j]
	if sum(rows) != sum(columns):
		return
	if len(rows) == 1:
		yield [columns]
	else:
		for top_row in topRow(rows[0], columns):
			for array in arrays(rows[1:], [columns[i] - top_row[i] for i in range(len(columns))]):
				yield [top_row] + array
				
				
# Console Application:
if __name__ == "__main__":
	print("Press q to quit, b to go back, enter integers separated by commas")
	
	while(1):
	
		step = 0
	
		if step == 0:
			rows = input("Enter the row sequence: ")
			if rows == "q":
				break
			elif rows == "b":
				continue
			else:
				try:
					rows = [int(number) for number in rows.split(",") if number != ""] 
					step += 1
				except:
					print("Invalid input: enter integers separated by commas")
					continue
		
		if step == 1:
			columns = input("Enter the column sequence: ")
			if columns == "q":
				break
			elif columns == "b":
				step -= 1		
			else:
				try:
					columns = [int(number) for number in columns.split(",") if number != ""] 
					step += 1
				except:
					print("Invalid input: enter integers separated by commas")
					continue
				
		if step == 2:
			if sum(rows) != sum(columns):
				print("Error: Sum of sequences do not match!")
				continue
			
			count = 0
			for matrix in arrays(rows, columns):
				print(np.array(matrix), "\n")
				count += 1
				
			print(f"{count} arrays printed.")
				
			
			
				
