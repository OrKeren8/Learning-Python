fisrt = ['Or', 'Gal', 'Liron']
last = ['Keren', 'Kantor', 'Attal']

# this line makes a list of tuples which every argument has one first name and one last name from the two lists
names = zip(fisrt, last)

for f, l in names:
    print(f, l)
