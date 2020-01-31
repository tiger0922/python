items = []
while True:
    print('Enter items ' + str(len(items) + 1) + ':')
    item = input()
    if item == '':
        break
    items.append(item)

string = items[0]
for i in range(1, len(items)):
    if i == len(items) - 1:
        string = string + ' and ' + items[i]
    else:
        string = string + ', ' + items[i] 

print('List: ', items)
print(string)

