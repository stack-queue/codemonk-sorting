from operator import itemgetter

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

num_dict = []
for num in input().split():
    num_dict.append({'number': int(num), 'mod': int(num) % k})
    
output_dict = sorted(num_dict, key = itemgetter('mod'))

print(" ".join(str(num['number']) for num in output_dict))
