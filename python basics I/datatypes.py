# Fundamental data types
# simple data types
# * int and float
# arithmetic operations
3 + 4 # addition
3 - 4 # substraction
3 * 4 # multiplication
3 / 4 # division
3 ** 4 # exponents 
3 // 4 # rounded division
3 % 4 # the rest of the division
# complex
complex(3, 2) # 3 + 2j ( j being the imaginary unit )

# *  variable (snake_case, starts with lowercase or Underscore, case sensitive, keywords are already taken)
# * constants 
PI = 3.14 # a convention for constants ( all uppercase )
# Dunder variables ( these are made to be left alone )

# * infinite assignment
a, b, c, d = 1, 2, 3, 4 # goes infinitely and for all types

# expressions => a piece of code that produces a values
# statement => a command of code that performs some kind of action

# * augmented assignment operator
x = 5
x += 2 # => x = x + 2
x -= 2 # => x = x - 2
x *= 2 # => x = x * 2
x /= 2 # => x = x / 2
x **= 2 # => x = x ** 2
x //= 2 # => x = x // 2
x %= 2 # => x = x % 2

# * complex datatypes
# *  strings
string = "A bunch of characters" # defining a string
long_string = """ """ # long string ( same with long comments )
super_long_string = string + long_string # strings are concatinatable
"Hello" + 5 # but only with other strings 
string = '\t [tab] that\'s \n \'long\'a string'  # escape sequences

# formatted strings
name = "Fawaz"
age = 18
print(f"hi {name}. You are {age} years old!") # python 3 -> recommended
print("hi {1}. You are {0} years old!".format(age, name)) # variables in format are indexed, we can chose which goes where with index
print("hi {name2}. You are {0} years old!".format(age, name2 = "Stippy")) # when defining a var inside format() we must use it's name

# * Most used string methods
name.capitalize()
name.count("a", 0, len(name)) # 2
name.endswith("z") # True
name.find("a") # 1, the index of the first occurrence  of "a"
name.index("w") # 2
name.replace("z", "s")
# https://www.w3schools.com/python/python_ref_string.asp for the full list

# * lists ( most basic data structure )
nums = [0, 1, 2, 3, 4, 5] # creating a list
nums_reference = nums # creating a list reference ( changes here affect the mother list )
nums_copy = nums[:] # creating an independent copy of a list
# * list methods
nums.append(6)
nums.extend([8, 9, 10])
nums.insert(7, 7) # insert(index, object)
nums.remove(0)
nums.pop(9) # pop(index)
nums.index(3, 1, 5) # index(object, start, end[excluded])
nums.count(4)
nums.sort() # sort(key:function, reverse:bool) -> the key is a function
sorted_nums = sorted(nums) # a sorted copy of nums (this is a function not a method)
nums.reverse() # nums = nums[::-1] 
nums_copy = nums.copy()
nums.clear() # nums = []
