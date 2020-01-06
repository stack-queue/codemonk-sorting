from collections import Counter 

n_testcases = int(input())

for i in range(n_testcases):
    n = int(input())
    heights = []
    for height in input().split():
        heights.append(int(height))
  
    c = Counter(heights)
    most = c.most_common()
    h1 = most[0][1]
    h2 = most[-1][1] 
    
    if abs(h1 - h2) == 0:
        print(-1)
    else:
        print(abs(h1 - h2))
