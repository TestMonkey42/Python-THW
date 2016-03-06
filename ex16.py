from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# r = read, w = write, a = append

target = open(filename, "w")

# print "Truncating the file. Goodbye!"
# target.truncate()

# request and read the three lines
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write the lines to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# reduce the previous 6 lines to 1 line
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# How about this one - preferable???
target.write("%s\n%s\n%s\n" %(line1,line2,line3))

print "And finally, we close it."
target.close()