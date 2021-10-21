#Creating lists
my_list = ['foo', 4, 5, 'bar', 0.4]
my_nested_list = ['foobar', ['baz', 'qux'], [0]]

#Accessing list values
my_list[2] # 5
my_list[-1] # 0.4
my_list[:2] # ['foo', 4, 5]
my_nested_list[2] # ['baz', 'quz']
my_nested_list[-1] # [0]
my_nested_list[1][1] # 'qux'

#Modifying lists
my_list.append(x) # append x to end of list
my_list.extend(iterable) # append all elements of iterable to list
my_list.insert(i, x) # insert x at index i
my_list.remove(x) # remove first occurance of x from list
my_list.pop([i]) # pop element at index i (defaults to end of list)
my_list.clear() # delete all elements from the list
my_list.index(x[, start[, end]]) # return index of element x
my_list.count(x) # return number of occurances of x in list
my_list.reverse() # reverse elements of list in-place (no return)
my_list.sort(key=None, reverse=False) # sort list in-place
my_list.copy() # return a shallow copy of the list