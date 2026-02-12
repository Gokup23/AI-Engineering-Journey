>>> age = int(21)
>>> print(age)
21
>>> height = float(6)
>>> print(height)
6.0
>>> g = 2+3j
>>> print(g)
(2+3j)
>>> base = int(input("Enter base: "))
Enter base: 23
>>> height = int(input("Enter height: "))
Enter height: 23
>>> Area = 0.5*base*height
>>> print(f"The area of the triangle is {Area}")
The area of the triangle is 264.5
>>> a = int(input("Enter Side a: "))
Enter Side a: 23
>>> b = int(input("Enter Side b: "))
Enter Side b: 23
>>> c = int(input("Enter Side c: "))
Enter Side c: 23
>>> perimeter = a+b+c
>>> print(f"The perimeter of the triangle is {perimeter}")
The perimeter of the triangle is 69
>>> length =int(input("Enter Length: "))
Enter Length: 23
>>> width =int(input("Enter width: "))
Enter width: 23
>>> area = length*width
>>> print(f"Area of rectangle is {area}")
Area of rectangle is 529
>>> radius = int(input("Enter radiush: "))
Enter radiush: 23
>>> area = 3.14*(r**2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'r' is not defined
>>> area = 3.14*(radiush**2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'radiush' is not defined
>>> area = 3.14*(radius**2)
>>> print(f"Area of circle is {area}")
Area of circle is 1661.0600000000002
>>> slope = 2 
>>> y = -2
>>> x = -y/slope
>>> print(f"slope:{slope}")
slope:2
>>> print(f"y intercept:{y}")
y intercept:-2
>>> print(f"x intercept:{x}")
x intercept:1.0
>>> x1,y1,x2,y2=2,2,6,10
>>> slope = m
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'm' is not defined
>>> m = slope
>>> m = (y2-y1)/(x2-x1)
>>> print(f"Slope is {m}")
Slope is 2.0
>>> d = ((x1-y1)**2 + (x2-y2)**2)**0.5
>>> print(f"Euclidean distance is: {d}")
Euclidean distance is: 4.0
>>> if slope ==m:
...     print("Both slopes are equal")
... else:
...     print("Not equal slopes")
... 
Both slopes are equal
>>> y = (x**2 + 6*x + 9)
>>> 0 = y
  File "<stdin>", line 1
    0 = y
    ^
SyntaxError: cannot assign to literal
>>> y = 0
>>> print(x)
1.0
>>> y = (x**2 + 6*x + 9)
>>> x = -3
>>> print(y)
16.0
>>> #Assign x first then y
>>> len('python')
6
>>> len('dragon')
6
>>> if 'on' in 'python' and 'dragon':
...    print(Yes)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'Yes' is not defined
>>> if 'on' in 'python' and 'dragon':
...     print("Yes")
... 
Yes
>>> if 'jargon' in 'I hope this course is full of jargon':
...    print(True)
... 
True
>>> if 'on' not in 'python' and 'dragon':
...     print(true)
... else:
...     print(false)
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
NameError: name 'false' is not defined
>>> length = len('python')
>>> length = length.float
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'float'
>>> length = float(length)
>>> length = string(length)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> length = str(length)
>>> print(type(length))
<class 'str'>
>>> num = 4
>>> if num%2 == 0:
...  print('even')
... 
even
>>> converted_value = int(2.7)
>>> floor_division = 7//3
>>> if converted_value == floor_division:
...    print('y')
... 
y
>>> if type('10') == type(10):
...  print('y')
... 
>>> if int('9.8') == 10:
...  print('y')
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9.8'
>>> hours = int(input("Enter hours"))
Enter hours23
>>> rate = int(input("Rate per hour:"))
Rate per hour:23
>>> print(f"Weekly earning: {hours*rate}")
Weekly earning: 529
>>> seconds_in_year=60*60*24*355
>>> years = int(input("Enter years:"))
Enter years:23
>>> print(f"Seconds given: {years*seconds_in_year}")
Seconds given: 705456000
>>> for i in range(1,6):
...     print(i, i**0, i**1, i**2, i**3)
... 
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
>>> 

"""
Questions.
1.Declare your age as integer variable
2.Declare your height as a float variable
3.Declare a variable that store a complex number
4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
6.The perimeter of the triangle is 12
7.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
8.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
9.Calculate the slope, x-intercept and y-intercept of y = 2x -2
10.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
11.Compare the slopes in tasks 8 and 9.
12.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
13.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
14.Use and operator to check if 'on' is found in both 'python' and 'dragon'
15.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
16.There is no 'on' in both dragon and python
17.Find the length of the text python and convert the value to float and convert it to string
18.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
19.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
20.Check if type of '10' is equal to type of 10
21.Check if int('9.8') is equal to 10
22.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
23.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
24.Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""