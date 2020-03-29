def swap_char(input, i, j):
  # not optimal as we are constructing new string objects
    t = list(input)
    temp = t[i]
    t[i] = t[j]
    t[j] = temp
    return ''.join(t)

def permute_string_rec(input, current_index, ending_index):
  print("in function: ",input, current_index, ending_index)
  if current_index == ending_index:
    print (input)
    return

  for i in range(current_index, ending_index + 1):
    print('in for loop ci ',current_index)
    swapped_input = swap_char(input,current_index,i);
    permute_string_rec(swapped_input, 
            current_index + 1, ending_index);

def permute_string(input):
  print('in permute_string')
  permute_string_rec(input, 0, len(input) - 1)

permute_string('BAD')

"""
0 0 3
1 1 3
BAD
2 1 3
BDA
1 0 3
1 1 3
ABD
2 1 3
ADB
2 0 3
1 1 3
DAB
2 1 3
DBA
"""