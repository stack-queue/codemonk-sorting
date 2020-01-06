n_testcases = int(input())

for i in range(n_testcases):
    n = int(input())
    heights = []
    for height in input().split():
        heights.append(int(height))
    
    set_heights = set(heights)
    
    h1, h2 = None, None
    for set_height in set_heights:
        temp = heights.count(set_height)
        
        if h1 == None:
            h1 = temp
        elif h1 > temp:
            h1 = temp
        if h2 == None:
            h2 = temp
        elif h2 < temp:
            h2 = temp
        
        for i in range(temp):
            heights.remove(set_height)
    
    if abs(h1 - h2) == 0:
        print(-1)
    else:
        print(abs(h1 - h2))
