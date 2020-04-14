file_write = open('sample.txt', 'w')
file_write.write("writing some stuff for check\n")
file_write.write('i dont like beacon')
file_write.close()


file_read = open('sample.txt', 'r')
text = file_read.read()
print(text)


file_read.close()