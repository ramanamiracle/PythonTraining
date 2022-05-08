f = open('sample.txt', 'r')
w = open('out.txt', mode='w')

for line in f.readlines():
    w.write(line)

f.close()
w.close()


# with open('sample.txt', 'r') as infile, open('out.txt', 'w') as outfile:
#     for line in infile:
#         outfile.write(line)

