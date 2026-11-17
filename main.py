# import numpy as np
# # a = np.random.uniform((3,2))
# a = np.random.normal(0,10, 25)
# b= np.reshape(a,(5,5))
# print(a)
# print(b)

# print(help(np.random.normal))

# fruits = ['apple', 'banana', 'cherry']

# fruits.append('orange')
# print(dir(fruits))
# print(help(fruits))


# # إنشاء قائمة بالأرقام الزوجية فقط
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)
# # النتيجة: [0, 2, 4, 6, 8]
# squares = {x: x**2 for x in range(1, 5)}
# print(squares)

names = ["nada", "mohammed", "sara"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
    
    
students = ["nada", "zahrar"]
scores = [95, 88]
for student, score in zip(students, scores):
    print(f"{student}: {score}")
    