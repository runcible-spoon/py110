'''
Given the following data structure, write some code to return a list that contains the colors of the 
fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.
'''

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

expected = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]




def get_descriptions(dictionary):
    new_list = []

    for produce in dictionary.values():
        if produce['type'] == 'fruit':
            new_list.append( [ color.capitalize() for color in produce['colors'] ] )
        else:
            new_list.append( produce['size'].upper() )
    return new_list

print(get_descriptions(dict1))