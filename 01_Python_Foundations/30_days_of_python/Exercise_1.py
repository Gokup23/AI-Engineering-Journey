# Day 2 : 30 days of python
# Variables and built-in functions

#level1
>>> first_name = "Gopal"
>>> last_name = "Parik"
>>> Full_name = first_name + last_name
>>> country = "INDIA"
>>> city = "Pune"
>>> Age = 21
>>> Year = 2026
>>> is_married = "No"
>>> is_true = 1
>>> is_light_on = 1
>>> a,b,c = 2,4,"Gopal23"
>>> print(Full_name)
GopalParik
>>> type(first_name)
<class 'str'>
>>> type(last_name)
<class 'str'>
>>> type(Full_name)
<class 'str'>
>>> type(country)
<class 'str'>
>>> type(city)
<class 'str'>
>>> type(Age)
<class 'int'>
>>> type(Year)
<class 'int'>
>>> type(is_married)
<class 'str'>
>>> type(is_light_on)
<class 'int'>

#level2
>>> len(first_name) == len(last_name)
True
>>> num_one,num_two = 5,4
>>> variable_total = num_one+num_two
>>> variable_diff = num_one-num_two
>>> variable_product = num_one*num_two
>>> variable_division = num_one/num_two
>>> variable_remainder = num_one%num_two
>>> variable_exp = num_one ** num_two
>>> variable_floor_division = num_one//num_two
>>> radius_circle = 30
>>> Area_circle =(3.14*radius_circle*radius_circle)
>>> print(Area_circle)
2826.0
>>> circum_of_circle =(2*3.14*radius_circle)
>>> print(circum_of_circle)
188.4
>>> r = int(input(f"Enter Radius: "))
Enter Radius: 23
>>> a_of_circle = (3.14)*(r**2)
>>> print(a_of_circle)
1661.0600000000002
>>> F_name = input("Enter First Name:")
Enter First Name:greg
>>> L_name = input("Enter last name:")
Enter last name:Plitt
>>> Country = input("Enter country : ")
Enter country : INDIA
>>> Age_ = input("Enter your age:")
Enter your age:21
>>> print(F_name,L_name,Country,Age)
greg Plitt INDIA 21
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

>>> 


"""
Questions:- 

1.Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2.Write a python comment saying 'Day 2: 30 Days of python programming'
3.Declare a first name variable and assign a value to it
4.Declare a last name variable and assign a value to it
5.Declare a full name variable and assign a value to it
6.Declare a country variable and assign a value to it
7.Declare a city variable and assign a value to it
8.Declare an age variable and assign a value to it
9.Declare a year variable and assign a value to it
10.Declare a variable is_married and assign a value to it
11.Declare a variable is_true and assign a value to it
12.Declare a variable is_light_on and assign a value to it
13.Declare multiple variable on one line

Exercises: Level 2
1.Check the data type of all your variables using type() built-in function
2.Using the len() built-in function, find the length of your first name
3.Compare the length of your first name and your last name
4.Declare 5 as num_one and 4 as num_two
5.Add num_one and num_two and assign the value to a variable total
6.Subtract num_two from num_one and assign the value to a variable diff
7.Multiply num_two and num_one and assign the value to a variable product
8.Divide num_one by num_two and assign the value to a variable division
9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10.Calculate num_one to the power of num_two and assign the value to a variable exp
11.Find floor division of num_one by num_two and assign the value to a variable floor_division
12.The radius of a circle is 30 meters.
13.Calculate the area of a circle and assign the value to a variable name of area_of_circle
14.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15.Take radius as user input and calculate the area.
16.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""