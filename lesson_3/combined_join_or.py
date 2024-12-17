def join_or(sequence, delimiter=', ', conjunction='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {conjunction} {sequence[1]}"
        
    zipped_list = list(zip(sequence, [delimiter for _ in range(len(sequence))]))
    zipped_list.insert(-1, conjunction + ' ')
    return ''.join([ str(element) for sublist in zipped_list
                                    for element in sublist ])[:-2]

print(join_or([1, 2, 3]), join_or([1, 2, 3]) ==  "1, 2, or 3")
print(join_or([1, 2, 3], '; '), join_or([1, 2, 3], '; ') == "1; 2; or 3")         
print(join_or([1, 2, 3], ', ', 'and'), join_or([1, 2, 3], ', ', 'and') == "1, 2, and 3")  
print(join_or([]), join_or([]) == "")                
print(join_or([5]), join_or([5]) == "5")                
print(join_or([1, 2]), join_or([1, 2]) == "1 or 2")
