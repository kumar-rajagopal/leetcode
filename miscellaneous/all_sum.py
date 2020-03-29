def print_all_sum_rec(target, current_sum, start, output):
  print('calling all sum rec')
  if current_sum == target:
    print('cs == targ ',output)

  for i in range(start, target):
    temp_sum = current_sum + i
    print("csi ",temp_sum, current_sum, i)
    if temp_sum <= target:
      #print('in if')
      output.append(i)
      print_all_sum_rec(target, temp_sum, i, output)
      #print("out: ",output)
      del output[len(output)-1]
      #print("out del: ",output)
    else:
      #return
      continue

def print_all_sum(target):
  print('in pas')
  output = [];
  print_all_sum_rec(target, 0, 1, output)

print_all_sum(4)
"""
in pas
calling all sum rec
csi  0 1
in if
calling all sum rec
csi  1 1
in if
calling all sum rec
csi  2 1
in if
calling all sum rec
csi  3 1
in if
calling all sum rec
cs == targ  [1, 1, 1, 1]
csi  4 1
final
out:  [1, 1, 1, 1]
out del:  [1, 1, 1]

csi  3 2
final
out:  [1, 1, 1]
out del:  [1, 1]
csi  2 2
in if
calling all sum rec
cs == targ  [1, 1, 2]
csi  4 2
final
out:  [1, 1, 2]
out del:  [1, 1]
csi  2 3
final
out:  [1, 1]
out del:  [1]
csi  1 2
in if
calling all sum rec
csi  3 2
final
out:  [1, 2]
out del:  [1]
csi  1 3
in if
calling all sum rec
cs == targ  [1, 3]
csi  4 3
final
out:  [1, 3]
out del:  [1]
out:  [1]
out del:  []
csi  0 2
in if
calling all sum rec
csi  2 2
in if
calling all sum rec
cs == targ  [2, 2]
csi  4 2
final
out:  [2, 2]
out del:  [2]
csi  2 3
final
out:  [2]
out del:  []
csi  0 3
in if
calling all sum rec
csi  3 3
final
out:  [3]
out del:  []

"""