'''
### Leftover Blocks

## Step 1: Understand the Problem

You have a number of building blocks that can be used to build a 
valid structure. There are certain rules about what determines a valid 
structure:

- The building blocks are [cubes](https://en.wikipedia.org/wiki/Cube).
- The structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, 
calculates the number of blocks left over after building the tallest 
possible valid structure.

### Tasks

You are provided with the problem description above. Your tasks for this step are:

- Make notes of your mental model for the problem, including:
    - inputs and outputs.
    - explicit and implicit rules.
- Write a list of clarifying questions for anything that isn't clear.
'''

# answers
'''inputs: integer representing number of supplied blocks
outputs: integer representing the numer of blocks leftover after building 
tallest possible structure w/ input number blocks

explicit requirements:
    - structure composed of layered cubes. 
    - cubes staggered such that one cube requires four beneath it
    - no gaps between cubes
implicit requirements:
    - some input numbers leave 0 leftover after building tallest possible strucutre
    - a "valid" layer is one that is a flat sheet of cubes with no space between any given cube and its neighbor
    - layer number correlates with blocks in a layer
    - number of blocks in a layer is: layer number * layer number


clarifying questions:
    - input is always positive integer?
    - null input results in null output?'''



'''
## Step 2: Examples and test cases

You are provided with the following test cases for this problem.

### Test Cases
'''

'''
Regarding your initial mental model and questions from Step 1, make 
some notes about the test cases. Do the test cases confirm or refute 
different elements of your original analysis and mental model? Do they 
answer any of the questions that you had, or do they perhaps raise 
further questions?

'''

#answers
''' 
notes on test cases: 
    - Confirms null input -> null output
    - confirms that some inputs result in no leftovers
    - Adds new expectation in output: only ever between 0 and 3
'''



'''
## Step 3: Data Structures

For this step, use your analysis so far to make notes regarding 
whether you might need to use any particular data structures as part of 
your solution. If so, make notes on which ones.
'''

# answer

'''
data structures:
    list of cubes per layer:
    - [1, 4, 9, ... ]
    or list of cubes per side per layer:
    - [1, 2, 3, ... ]
'''



'''
## Step 4: Algorithm

For this step, use your analysis of the problem so far to write out a
 high-level algorithm that solves the problem at an abstract level. 
Avoid too much implementation detail at this stage.
'''

# answer
'''
1. Take the input number n as "number of remaining blocks".
2. Start "current layer number" as 0
3. If input equals "current layer number", return number. Else, add 1 to "current layer number". 
5. Set "blocks in current layer" to "curent_layer_number" squared.
6. Subtract "blocks in current layer" from "number of remaining blocks.
7. If "number of remaining blocks" is greater than or equal to "number of blocks 
4. Until it does, add to s (n + 1)**2. Subtract again. 
'''

'''
## Step 5: Implement a Solution in Code

Based on all of your notes and analysis so far, implement a working 
solution in Python. Your solution should pass all of the test cases 
provided.
'''

def calculate_leftover_blocks(input_blocks):
    curent_layer = 0
    remaining_blocks = n

    required_blocks = (curent_layer + 1) ** 2

    while remaining_blocks >=  required_blocks:
        remaining_blocks -= required_blocks
        curent_layer += 1
        required_blocks = (current_layer_number + 1) ** 2

    return remaining_blocks

    number_of_blocks_remaining = input_blocks
    current_layer_number = 0

    if number_of_blocks_remaining == current_layer_number:
        return number_of_blocks_remaining
    
    current_layer_number += 1
    blocks_to_complete_layer = current_layer_number * current_layer_number

    if number_of_blocks_remaining >= blocks_to_complete_layer:
        number_of_blocks_remaining -= blocks_to_complete_layer
    else:
        return number_of_blocks_remaining



print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
