'''
Define a recursive function that, takes in an index n will calculate the n-th number in the fibonacci sequence.
The fibonacci sequence is defined as 
f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)
The index is to be read from the standard input and 
the fibonacci number at that index is to be printed
to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

#Initialising a dictionary with a fibonacci series of 4 elements
fib_dict = {
	0: 0,
	1: 1,
	2: 1,
	3: 2
}

# Define this recursive function to return the expected output
# Do not print it from this function
def fib_sequence(num):
	# to be completed
	#if file is executed directly from terminal and not from pytest.
	if __name__ == '__main__':
		n = int(input("Enter Index: "))
		if n in fib_dict:
			print(fib_dict[n])
		if n == 1 or n == 2:
			return 1	
		else:
			answer = fib_sequence(n - 1) + fib_sequence(n - 2)
			fib_dict[n] = answer
			print (answer)
			return answer
	else:
		if num == fib_dict:
			return fib_dict[num]
		if num == 1 or num == 2:
			return 1	
		else:
			answer = fib_sequence(num - 1) + fib_sequence(num - 2)
			fib_dict[num] = answer
			return answer					
	


#write code to accept user input, call the function and print the result
