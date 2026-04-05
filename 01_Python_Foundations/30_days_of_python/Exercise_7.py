#Dictonaries

dog = {}

dog.update({'first_name':'Sam',
            'last_name':'ginga',
            'gender':'male',
            'age':'2',
            'marital status':'Nope',
            'skills':'digging',
            'country':'istanbul',
            'city':'lamington',
            'address':'beside me'})
print(dog)

print(len(dog))

print(dog['skills'])
print(type(dog['skills']))

print(dog.keys())

print(dog.values())

print(dog.items())

del dog['marital status']

del dog
print(dog)