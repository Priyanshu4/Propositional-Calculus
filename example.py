# This file contains the example code from the README.md file.

# Import the propositionalcalc module
import propositionalcalc as pc

# Let's create some expressions.
# The variables in our expressions can be single letters or entire words like we use below.
# Note that 'true' and 'false' are reserved words and cannot be used as variable names.

# If it is raining, the ground is wet and it is not sunny
raining_then_wet = pc.parse_proposition('raining -> (wet & ~sunny)') 

# If it is not raining, the ground is dry
no_rain_then_dry = pc.parse_proposition('~raining -> ~wet')

# If and only if the ground is wet, then the tennis game will be cancelled
wet_then_no_tennis = pc.parse_proposition('wet <-> ~tennis')

# If the tennis game is not cancelled, then we do not have time to go to the movies or go hiking.
tennis_then_no_activities = pc.parse_proposition('tennis -> ~(movie || hiking)')

# Can we conclude that if we go to the movies, it is not sunny?
conclusion = pc.parse_proposition('movie -> ~sunny')

# Let's check the validity of this argument.
# The premises of the argument are the propositions which are given to be true.
argument = pc.Argument([raining_then_wet, 
                        no_rain_then_dry,
                        wet_then_no_tennis,
                        tennis_then_no_activities], 
                        conclusion=conclusion)

print(argument.get_truth_table()) # prints the truth table for the argument
print(argument.is_valid()) # prints True, indicating that the argument is valid







