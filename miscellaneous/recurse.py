def recurse(num):

    if num > 1:
        print('num val')
        return
    for i in range(0,6):
        print('here ')
        if i // 2 > 1:
            recurse(i)
            print('after recurse')
recurse(0)