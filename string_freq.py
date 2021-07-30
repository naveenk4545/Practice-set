string = input()
sub = input()
size = len(sub)
count = 0
for i in range(len(string)-size+1):
    if(string[i:i+size]==sub):
        count += 1
print(count)