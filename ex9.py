# Here's some new strange stuff, remember to type it exactly

days =  "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print "Here are the days: %s" % days
print "Here are the months: %s" % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print """
Trying again but with format characters.
There's something going on here.
With the three double-quotes. 
%s
%s
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" % (days, months)