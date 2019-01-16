list1 = ['a', 'b', 'c']
list2 = ['a', 'b', 'c', 'c', 'c']
results = {}
for i in list1:
        results[i] = list2.count(i)
