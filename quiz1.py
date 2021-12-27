number = int(input('enter a num    '))

#generate list range from 1 - whatever is input plus 1 
listofdiv = list(range(1,number+1))


new_list = []

# for loop to go thru whole list range created, has to dived evenly so % which will need to have remainder  = 0

for num in listofdiv:
    if number%num==0:
# add to empty
        new_list.append(num)


print(new_list)