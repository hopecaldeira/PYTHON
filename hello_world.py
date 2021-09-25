# 1. TASK: print "Hello World"
print( "Hello " + "World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Hope"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 1
print( "Hello", name )	# with a comma
print( "Hello " + str(1) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string
#4a bonus prompts
fave_food3 = "poke"
fave_food4 = "pho"
print("I love to eat {} and {}.".format(fave_food3, fave_food4))
#4b bonus prompts
fave_food5 = "french fries"
fave_food6 = "waffles"
print(f"I love to eat {fave_food5} and {fave_food6}.")