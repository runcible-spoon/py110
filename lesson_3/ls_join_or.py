def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"

    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    print(leading_items)
    return print(f'{leading_items}{delimiter}{word} {sequence[-1]}')

print(join_or([1, 2, 3]) ==  "1, 2, or 3")
'''print(join_or([1, 2, 3], '; '), join_or([1, 2, 3], '; ') == "1; 2; or 3")         
print(join_or([1, 2, 3], ', ', 'and'), join_or([1, 2, 3], ', ', 'and') == "1, 2, and 3")  
print(join_or([]), join_or([]) == "")                
print(join_or([5]), join_or([5]) == "5")                
print(join_or([1, 2]), join_or([1, 2]) == "1 or 2")'''
