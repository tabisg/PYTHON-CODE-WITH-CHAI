#Iterates with index. show index 
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)


#zip()Combines two (or more) iterables
names = ['Alice', 'Bob']
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)


#. iter() and next()Manual iteration.
nums = iter([1, 2, 3])
print(next(nums))  # 1
print(next(nums))  # 2



#
import itertools

for i in itertools.combinations([1, 2, 3], 2):
    print(i)  # (1, 2), (1, 3), (2, 3)


