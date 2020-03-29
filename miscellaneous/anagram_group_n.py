from collections import defaultdict
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
i = 0
j = len(input) -1
seen = defaultdict(list)
print(input)
while i < j:
    item_1 = ''.join(sorted(input[i]))
    item_2 = ''.join(sorted(input[j]))
    print(item_1,item_2)
    if item_1 == item_2:
        seen[item_1].append(item_2)
        i += 1
    else:
        seen[item_1] = []
        seen[item_2] = []
    j -= 1
print(seen)