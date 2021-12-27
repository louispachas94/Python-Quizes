number = int(input('enter a num    '))
listofdiv = list(range(1,number+1))
new_list = []

for num in listofdiv:
    if number%num==0:
        new_list.append(num)
        
print(new_list)