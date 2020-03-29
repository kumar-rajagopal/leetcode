def binaryGap(N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)
        items = b[2:]
        i = 0
        j = 1
        max_item = 0
        print(items)
        while j < len(items):
            #print(items[j], j)
            if items[i] == 1 and items[j] == 1:
                #print('both equal')
                max_item = max(max_item, j)
                i = j
                j = j + 1
                print('1 ',max_item)
            elif items[i] == 1 and items[j] != 1:
                j += 1
                max_item = max(max_item, i)
                print('2 ',max_item)
            elif items[j] == 1 and items[i] != 1:
                max_item = max(i,j)
                print('3 ',max_item)
            else:
                i += 1
                j += 1
            print('m ',max_item)
        return max_item

print(binaryGap(22))
#10110