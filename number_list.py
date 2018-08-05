def find_reverse(numbers):
    #TODO: find the reverse of the list
    numbers.reverse()

    return numbers

def find_max(numbers):
    #TODO: find the maximum of the list
    highest = 0
    if len(numbers) == 0:
        return highest
    else:
        for i in numbers:
            if i > highest:
                highest = i    

    return highest

def find_min(numbers):
    #TODO: find the minimum of the list
    smallest = numbers[0]
    if len(numbers) == 0:
        print(0)
    elif numbers:
        for compare in numbers:
            if smallest >= compare:
                smallest = compare

    return smallest

    

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    sum = 0
    for i in numbers:
        sum = sum + i

    return sum       
    

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    count = 0
    sumofnum = 0
    for i in numbers:

        sumofnum = sumofnum + i
        count +=1

    average = sumofnum/count
    return average

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    numbers.sort()
    numbers.reverse()
    return numbers


def second_smallest(numbers):
    #TODO: find the second smallest
    
    #numbers.sort()

    lowest = numbers[0]
    sec_smallest = numbers[1]

    for i in numbers:
        if i < lowest:
            sec_smallest = lowest
            lowest = i
        elif lowest == sec_smallest:
            sec_smallest = i  
        elif i < sec_smallest and i > lowest:
            sec_smallest = i      
             

    return sec_smallest        


    


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list


    
    pass
