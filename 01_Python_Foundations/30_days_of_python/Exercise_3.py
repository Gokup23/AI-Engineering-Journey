>>> r = "Thirty"+"Days"+"of"+"python"
>>> print(r)
ThirtyDaysofpython
>>> g = 'Coding '+'For '+'All '
>>> print(g)
Coding For All 
>>> company = g
>>> print(company)
Coding For All 
>>> print(len(company))
15
>>> print(company.upper())
CODING FOR ALL 
>>> print(company.lower())
coding for all 
>>> print(company.capitalize().title().swapcase())
cODING fOR aLL 
>>> print(company[0:5])
Codin
>>> company.capitalize().title()
'Coding For All '
>>> company.find("Coding")
0
>>> print(company.replace('Coding','Python'))
Python For All 
>>> print(company.replace('All','Everyone'))
Coding For Everyone 
>>> print(company.split(' '))
['Coding', 'For', 'All', '']
>>> "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']
>>> print(company[0])
C
>>> print(len(company)-1)
14
>>> company[10]
' '
>>> words = company.split()
>>> letters = [w[0] for w in words]
>>> acronym = "".join(letters)
>>> print(acronym)
CFA
>>> company.index('C')
0
>>> company.index('F')
7
>>> "Coding For All People".rfind('l')
19
>>> 'You cannot end a sentence with because because because is a conjunction'.index('beca\
use')
31
>>> 'You cannot end a sentence with because because because is a conjunction'.rfind('beca\
use')
47
>>> phrase = 'You cannot end a sentence with because because because is a conjunction'
>>> print(phrase[phrase.index('because')])
b
>>> print(phrase[phrase.index('because'):phrase.rindex('is')])
because because because 
>>> 'Coding For All'.startswith('Coding')
True
>>> 'Coding For All'.endswith('coding')
False
>>> print('   Coding For All      '.strip())
Coding For All
>>> '30DaysOfPython'.isidentifier()
False
>>> 'thirty_days_of_python'.isidentifier()
True
>>> libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
>>> '#'.join(libraries)
'Django#Flask#Bottle#Pyramid#Falcon'
>>> print('I am enjoying this challenge. /n I just wonder what is next.')
I am enjoying this challenge. /n I just wonder what is next.
>>> print('I am enjoying this challenge.'+ '/n'+'I just wonder what is next.')
I am enjoying this challenge./nI just wonder what is next.
>>> print('I am enjoying this challenge.\nI just wonder what is next.')
I am enjoying this challenge.
I just wonder what is next.
>>> print('Name/tAge/tCountry/tCity/t/nVinzeku/t230/tSwitzerland/tHelsinki')
Name/tAge/tCountry/tCity/t/nVinzeku/t230/tSwitzerland/tHelsinki
>>> print('Name /t Age /t Country /t City /t /n Vinzeku /t 230 /t Switzerland /t Helsinki\
')
Name /t Age /t Country /t City /t /n Vinzeku /t 230 /t Switzerland /t Helsinki
>>> print('Name \t Age \t Country \t City \nVinzeku \t 230 \t Switzerland \t Helsinki')
... 
Name 	 Age 	 Country 	 City 
Vinzeku 	 230 	 Switzerland 	 Helsinki
>>> print('radius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 \
is 314 meters square')
radius = 10 
area = 3.14 * radius ** 2 
The area of a circle with radius 10 is 314 meters square
>>> a=2
>>> b=3
>>> print(f"{ a }+{ b } = {a+b}")
2+3 = 5
>>> print(f"{ a }-{ b } = {a-b}")
2-3 = -1
>>> print(f"{ a }*{ b } = {a*b}")
2*3 = 6
>>> print(f"{ a }/{ b } = {a/b}")
2/3 = 0.6666666666666666
>>> print(f"{ a }//{ b } = {a//b}")
2//3 = 0
>>> print(f"{ a }**{ b } = {a**b}")
2**3 = 8

'''
Questions:- 
1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3.Declare a variable named company and assign it to an initial value "Coding For All".
4.Print the variable company using print().
5.Print the length of the company string using len() method and print().
6.Change all the characters to uppercase letters using upper() method.
7.Change all the characters to lowercase letters using lower() method.
8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
9.Cut(slice) out the first word of Coding For All string.
10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
11.Replace the word coding in the string 'Coding For All' to Python.
12.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
13.Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
14.Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
15.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
16.The area of a circle with radius 10 is 314 meters square.
17.Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''