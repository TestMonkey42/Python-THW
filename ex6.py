# declares variable x and puts the decimal value 10 within the string
x = "There are %d types of people." % 10
# variable binary has value of string "binary"
binary = "binary"
# variable do_not has value of string "don't"
do_not = "don't"
# string put inside a string, this happens twice 1 , 2
# string variable y has variables 'binary' and 'do_not' put inside the string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# string put inside a string 3
print "I said: %r." % x
# string put inside a string 4
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# string put inside a string 5
print w + e