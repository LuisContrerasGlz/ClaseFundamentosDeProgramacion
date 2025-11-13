# W mode for write
write_file = open(r'FakeFile.txt', 'w')
write_file.write('This is our first sentence in our file.')
write_file.close()

# A for us to append to the file
append_file = open(r'FakeFile.txt', 'a')
append_file.write(' This is our Second sentence in our file.')
append_file.close()

# Write multi line

multi_line = """
This is the Fourth sentence.
This is the Fifth sentence.
This is the Sixth sentence.
"""

with open(r'FakeFile.txt', 'a') as append_file:
    append_file.write(multi_line)
