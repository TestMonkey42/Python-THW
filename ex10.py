tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
r_string = "I'm a \'fat\' stringy \"cat\"!!"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

fat_cat_single = '''
I'll do a single quote list:
\t* "Cat food"
\t* "Fishes"
\t* Catnip\n\t* Grass
I said "hello"
'''

print tabby_cat
print persian_cat
print backslash_cat
print r_string
print "sFormat Cat said: %s" % r_string
print "rFormat Cat said: %r" % r_string

print fat_cat
print fat_cat_single

# while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,