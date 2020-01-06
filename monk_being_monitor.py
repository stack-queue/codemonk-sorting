n_testcases = int(input())

for i in range(n_testcases):
    n = int(input())
    heights = []
    for height in input().split():
        heights.append(int(height))
    
    h1_heights = []
    for height in heights:
        h1_heights.append(height)
        
    h1 = None
    for height in h1_heights:
        temp = h1_heights.count(height)
        if h1 == None:
            h1 = temp
        elif h1 > temp:
            h1 = temp
            for i in range(temp):
                h1_heights.remove(height)
    
    h2_heights = []
    for height in heights:
        h2_heights.append(height)

    h2 = None
    for height in h2_heights:
        temp = h2_heights.count(height)
        if h2 == None:
            h2 = temp
        elif h2 < temp:
            h2 = temp
            for i in range(temp):
                h2_heights.remove(height)
    
    if abs(h1 - h2) == 0:
        print(-1)
    else:
        print(abs(h1 - h2))
