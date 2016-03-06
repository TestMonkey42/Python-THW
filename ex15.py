#  import the feature argv
from sys import argv

# two variables for the script
script, filename = argv

# Open the file (filename) and assign txt variable the file object
txt = open(filename)

# print the name of the file (filename)
print "Here's your file %r:" % filename
# read the contents of txt file object and print it
print txt.read()
txt.close()

# request the file name and assign to variable file_again
print "Type the filename again:"
file_again = raw_input("> ")
# Open the file_again file and assign txt_again variable the file object
txt_again = open(file_again)

# read the contents of txt_again and print it.
print txt_again.read()

txt_again.close()