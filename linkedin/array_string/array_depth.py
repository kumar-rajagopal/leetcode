arr = [1,[4,[6]]]
def depth(arr, count=0):
        print('len ',len(arr))

        for i in arr:
                if type(i) is list:
                        #print(i)
                        count += 1
                        depth(i, count)
                else:
                        count = 1
        if len(arr) >= 1:
                print(count)
        #return -1

print(depth(arr))
