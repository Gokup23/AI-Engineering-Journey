#Conditionals

#Exercise_level1

age = int(input("Enter your age: "))
if age >= 18:
    print(f"You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive")

my_age = 25
your_age = int(input("Enter your age mister: "))
if your_age < my_age :
    print(f"You are {my_age - your_age} younger than me :D ")
else:
    print(f"You are {your_age-my_age} older than me :/ ")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a ")
else:
    print("a is equal to b")

#Exercise_Level2

Score = int(input("Enter score to grade: "))
if Score >= 0 and Score <= 59:
    print("F")
elif Score >= 60 and Score <= 69:
    print("D")
elif Score >= 70 and Score <= 79:
    print("C")
elif Score >= 80 and Score <= 89:
    print("B")
elif Score >= 90 and Score <= 100:
    print("A")

month = str(input("Enter Month: "))
if month in ['September','October','November']:
    print("Autumn")
elif month in ['December','January','February']:
    print("Winter")
elif month in ['March','April','May']:
    print("Spring")
else:
    print("Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_req = str(input("Enter Fruit to add: "))
if fruit_req in fruits:
    print("Already in the list ! ")
else:
    fruits.append(fruit_req)

#Exercise_level3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print(person["skills"][3])

if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print("YES")
    else:
        print("NO")

if person['is_married'] == True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")