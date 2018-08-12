# loops

people = ['john', 'sarah', 'tim', 'bob']
for person in people:
    print('Current person', person)

# iterate by seq index

for i in range(len(people)):
    print('Current person', people[i])

for i in range(0, 10):
    print(i)

# while loop

count = 0 
while count <= 10:
    print('count:', count)
    count = count + 1   