string_k = input().split()
string = string_k[0]
k = int(string_k[1])

string_list = []
for i in range(len(string)):
    string_list.append(string[-(len(string) - i):])

print(sorted(string_list)[k - 1])
