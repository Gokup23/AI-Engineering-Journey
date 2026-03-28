# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise - level1

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Vincorp','Vinzenu','Vinkazz'])
print(it_companies)

it_companies.pop()

#remove() method removes the element if it exists, if it doesnt raises a keyerror
#dicard() method removed the element if it exists, if it doesnt no keyerror raised

#Level 2

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

A.update(B)
B.update(A)
print(A,B)

print(A.symmetric_difference(B))

del A,B,C

#Exercise 3

age_set = set(age)
print(len(age_set)) #length reduces as set only keeps non duplicate , unordred
print(len(age))

'''
String can have letters,numbers inside quote or doublequote, text , a datatype
list is mutable, ordered , any type of elements can exist , square bracket
tuple is immutable , ordered , can keep elements of diff types , circle bracket
set is immutable , unordered , uses curly bracket , doesnt allow duplicates
'''

sentence = "I am a teacher and I love to inspire and teach people.".split()
sentence_convert_to_set = set(sentence)
print(len(sentence_convert_to_set))