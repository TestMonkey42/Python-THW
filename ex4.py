# number of cars available
cars = 100
# how many people a car can hold
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars that will not be driven
cars_not_driven = cars - drivers
# number of cars that will be driven. this is the number of drivers available
cars_driven = drivers
# total number of people who will be transported
carpool_capacity = cars_driven * space_in_a_car
# number of passengers per car to get all passengers transported
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"
# what about: print "Hey there." % "you"
