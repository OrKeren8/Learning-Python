# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext_and_mt = {}  # all of the file extensions and thier mime type
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_and_mt[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    fname = fname.lower()
    if '.' in fname:
        fname = fname.split('.')
        if fname[len(fname)-1] in ext_and_mt:
            print(ext_and_mt[fname[len(fname)-1]])
        else:
            print('UNKNOWN')
    else:
        print('UNKNOWN')