# Propositional-Calculus

## About
This repository contains a Python package, `propositionalcalc`, for parsing propositional logic expressions and checking the validity of logical arguments. I developed this package for a discrete math honors project.

## What is Propositional Calculus/Logic?
Propositional calculus is a system of symbolic logic. The term is interchangeable with propositional logic.
Propositions are statements in propositional logic which are either true or false.
Propositions may contain boolean variables, the constants true and false, and the following logical connectives: negation (not), conjunction (and), disjunction (or), conditional (if), and biconditional (if and only if). An argument in propositional calculus is a set of propositions called premises, which are given to be true, and a proposition called the conclusion, whose truth value is to be determined. If the conclusion can be determined to be true as a result of the premises, the argument is valid. Otherwise, it is invalid. 

## Usage
This library is not on `pip`, so it must be installed simply by downloading the `propositonalcalc` folder into your project. No other dependencies are required.
The following example shows how to use the library once installed.

```python
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
```
