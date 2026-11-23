
from itertools import product

# Knowledge Base
# Example:
# P = It is raining
# Q = The ground is wet
# R = It is cloudy

# Rules:
# P -> Q
# R -> P
# R is true

KB = [
    lambda m: (not m['P'] or m['Q']),
    lambda m: (not m['R'] or m['P']),
    lambda m: m['R']
]

# Given Query
# Query: Q (The ground is wet)

query = lambda m: m['Q']

# Propositional symbols
symbols = ['P', 'Q', 'R']


def entails(KB, query, symbols):

    # Generate all possible truth assignments
    for values in product([True, False], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        # Check whether the model satisfies KB
        if all(sentence(model) for sentence in KB):

            # Check whether query is true
            if not query(model):
                print("Counterexample found:", model)
                return False

    return True


# Display result
print("Knowledge Base:")
print("1. P -> Q")
print("2. R -> P")
print("3. R")

print("\nQuery: Q")

if entails(KB, query, symbols):
    print("\nKB entails the query.")
else:
    print("\nKB does not entail the query.")
