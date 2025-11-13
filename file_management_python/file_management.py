# W mode for write
write_file = open(r'FakeFile.txt', 'w')
write_file.write('This is our first sentence in our file.')
write_file.close()

# A for us to append to the file
append_file = open(r'FakeFile.txt', 'a')
append_file.write(' This is our Second sentence in our file.')
append_file.close()
