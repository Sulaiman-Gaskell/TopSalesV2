'          Top 2 3          '

import os

try:
    clear = lambda: os.system('clear')
except:
    clear = lambda: os.system('cls')



tItems = []
while True:
    clear()
    item = input('''Enter the following:
Item name
Number of item sales from last month
Number of item sales from the months before the last
Enter all on one line where each value is sperated by a single space

--> ''').split()
    tItems.append(item)
    clear()
    while True:
        try:
            again = input('''Add another item (y/n)?

--> ''').lower()
            if again == 'y' or again == 'n':
                break
            again = int('f')
            
        except:
            print('\nOops please try again\n')    


    if again == 'n':
        break
with open('Items.txt','w') as f:
    for item in tItems:
        f.write(','.join(item))
        f.write('\n')

clear()
print('Items being read from the text file:\n')
print(open('Items.txt').read())


#case one
print('\nCase one: Maximum sales ordered alphabetically\n')

case1 = sorted(tItems)
for item in case1:
    print(*('Max sale for',item[0],'is',item[1]) if int(item[1]) > int(item[2]) else('Max sale for',item[0],'is',item[2]))
    

    
#case two
print('\n\nCase two: Maximum sales ordered from highest to lowest\n')

case2 = []
for item in tItems:
	itemL = []
	itemL.append(item[0])
	if int(item[1]) > int(item[2]):
		itemL.append(item[1])
	else:
		itemL.append(item[2])
	case2.append(itemL)

case2.sort(key=lambda x: x[1])
case2.reverse()
for item in case2:
	print('Max sale for',item[0],'is',item[1])


#case three
print('\n\nCase three: Average sales ordered from highest to lowest\n')

case3 = []
for item in tItems:
	itemL = []
	itemL.append(item[0])
	itemL.append((int(item[1]) + int(item[2])) / 2)
	case3.append(itemL)

case3.sort(key=lambda x: x[1])
case3.reverse()
for item in case3:
	print('Average sale for',item[0],'is',item[1])




