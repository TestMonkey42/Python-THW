# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is acutually pretty pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    print "yo yo"


# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I got nuthin'."


Cuong = "Cuong"
print_two("Cuong", "Nguyen")
print_two_again(Cuong, "Nguyen")
print_one("First!")
print_none()
