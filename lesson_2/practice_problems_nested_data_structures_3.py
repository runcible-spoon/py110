'''Given the following code, what will the final values of a and b be? 
Try to answer without running the code.
'''
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

print('a = ', a, 'b =', b, 'lst =', lst) # 4, 1, [4, [1, 8]]


# a =  2 b = [3, 8] lst = [4, [3, 8]]
