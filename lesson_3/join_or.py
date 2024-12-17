def join_or(valid_choices, delimiter=', ', conjunction='or'):
    if not valid_choices:
        return ''
    elif len(valid_choices) == 1:
        return str(valid_choices[0])
    elif len(valid_choices) == 2:
        return ''.join([str(valid_choices[0]) + ' ', conjunction + ' ', str(valid_choices[1])])
    else:
        zipped_list = list(zip(valid_choices, [delimiter for _ in range(len(valid_choices))]))
        zipped_list.insert(-1, conjunction + ' ')
        joined_list = ''.join([ str(element) for sublist in zipped_list
                            for element in sublist ])
        return joined_list[:-2]

print(join_or([1, 2, 3]), join_or([1, 2, 3]) ==  "1, 2, or 3")
print(join_or([1, 2, 3], '; '), join_or([1, 2, 3], '; ') == "1; 2; or 3")         
print(join_or([1, 2, 3], ', ', 'and'), join_or([1, 2, 3], ', ', 'and') == "1, 2, and 3")  
print(join_or([]), join_or([]) == "")                
print(join_or([5]), join_or([5]) == "5")                
print(join_or([1, 2]), join_or([1, 2]) == "1 or 2")
