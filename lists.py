# Write a Python program to sum all the items in a list.
def add(list):
    sum =0
    for item in list:
         sum+=item
         return sum
list=[6,8,9,56,8]
print(add(list))




#  Write a Python program to find the largest number in a list.


def largest(list):
  return  max(list)

list = [345, 90, 236, 53,  123]    
print(largest(list))  
   
     
        

# #    Write a Python program to find the smallest number in a list.  

def smallest(list):
    return min(list)
list=[78,4500,73,92,72]
print(smallest(list))

# #  Write a Python program to remove duplicates from a list.
new_list = []
def duplicate(list):
    for num in list:
        
   

# #  Write a Python program to check if a list is empty.
# def empty(list): 
#     em=[]
#     if
#     # Write a Python program to reverse a list.
      def rev(list):
       list=[4,3,6,1,7,8]
list.reverse()
    
print(list)
# #  Write a Python program to count the number of occurrences
# # of an item in a list.

def counting(list):
 list=[4,5,6,7,8,4,3,1,2,4,6,7,5,4]
list.count(4)
print(list)
# Write a function that takes an unknown number of arguments and returns their sum.
def sum(*args):
   
    result = 0
    for number in args:
        result += number
    return result
 
 
#  Write a function that takes two arguments, the first being a string and the
# second being an unknown number of integers. The function should return a 
# new string where the integers have been added to the original string.
def add_to_string(string, *numbers):
    
    result = string
    for number in numbers:
        result += str(number)
    return result
add_to_string(2,7,9,5,9,43)


# Write a function that takes an unknown number of keyword arguments and
# returns a dictionary where the keys are the argument names and the values 
# are the argument values.
def create_dict(**kwargs):
   
    result = {}
    for key, value in kwargs.items():
        result[key] = value
    return result
dict(animal="dog", breed="golden retriever", age=3, color="golden")

# Write a function that takes a function and an unknown number of arguments, 
# and returns the result of calling the function with the arguments.

def apply_function(func, *args):
  
    return func(*args)

# Write a function that takes a list of integers and an unknown number of
# keyword arguments. The function should return a new list where each 
# integer in the original list has been multiplied by the value of
# the corresponding keyword argument.
def multiply_list(list, **kwargs):
    empty = []
    for num in list:
        for key, value in kwargs.items():
            if int(key) == len(empty):
                empty.append(num * value)
            else:
                empty[len(empty)-1] *= value
    return empty

# Write a function that takes a list of integers and an unknown number of 
# additional integers as arguments. The function should return the index
# of the first occurrence of the sum of the list and the additional integers
def index_of_occurence(list,*args):
    
    total = sum(list) + sum(args)
    for i, num in enumerate(list):
        if num == total:
            return i
    return -1  
lst = [1, 2, 3, 4]
index = index_of_occurence(lst, 5, 6)
print(index)

# Write a function that takes an unknown number of keyword arguments, each with 
# a string value. The function should concatenate all the strings and return 
# the resulting string.
def concatenate_strings(**kwargs):
    concatenated_string = ""
    for key, value in kwargs.items():
        concatenated_string += value
    return concatenated_string
concatenate_strings(first_name="Leila", last_name="Ashur")

    





   
   
       
    
  

    
