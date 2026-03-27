#Exercise - level1
empty_tuple = ()
empty_tuple1 = tuple()

brothers = ('jotaro','guts','max')
sisters = ('dora','reshma','disha')

siblings = brothers + sisters
print(siblings)

print(len(siblings))

family_members = list(siblings)
family_members.extend(['Gopal','Parik'])
print(family_members)

#Exercise - level2

siblings = family_members[0:3]
parents = family_members[3:8]

fruits = ('apple','banana','pomogranete')
vegetables = ('cucumber','bottleguard','carrot')
animal = ('bison','tiger','platypus')
food_stuff_tp = fruits+vegetables+animal
print(food_stuff_tp)

food_stuff_it = list(food_stuff_tp)
print(food_stuff_it)

print(food_stuff_it[len(food_stuff_it)//2])

print(food_stuff_it[0:3])
print(food_stuff_it[-1:-4:-1])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)