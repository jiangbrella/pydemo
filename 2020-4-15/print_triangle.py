# coding = utf-8
max_line = int(input())

for i in range(1,max_line + 1):
    print('*' * i)

last_line = max_line - 1 
while last_line > 0:
    print('*' * last_line)
    last_line -= 1

print('-' * 5)  
range_line = max_line * 2
for i in range(1,range_line + 1):
    if i > max_line:
        i = range_line - i 
    while i > 0:
        print('*',end='')
        i -= 1 
    print('')
    
