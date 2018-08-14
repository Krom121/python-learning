# open file

fo = open('opentest.txt', 'w')
# get some info
print('name:', fo.name)
print('is closed', fo.closed)
print('opening mode', fo.mode)
# Write to a file
fo.write('I love Python')
fo.write(' And Django')
# Close a file
fo.close()
# Append a file
fo = open('opentest.txt', 'a')
fo.write(' I also like SASS')
# Close file
fo.close()
# read from file
fo = open('opentest.txt', 'r+')
text = fo.read(15)
print(text)
fo.close()

# Create a file
fo = open('test2.txt', 'w+')
fo.write('this is my new file')
fo.close()