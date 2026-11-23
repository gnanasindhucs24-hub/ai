
# Resolution in Propositional Logic

# Knowledge Base:
# P -> Q
# Q -> R
# P
#
# Query: R

# Clauses in CNF:
# P -> Q  = ~P OR Q
# Q -> R  = ~Q OR R
# P       = P

KB = [
    {"~P", "Q"},
    {"~Q", "R"},
    {"P"}
]

# Given query
query = "R"


def resolve(ci, cj):
    """Apply resolution rule to two clauses."""
    resolvents = set()

    for literal in ci:
        if literal.startswith("~"):
            complement = literal[1:]
        else:
            complement = "~" + literal

        if complement in cj:
            new_clause = (ci - {literal}) | (cj - {complement})
            resolvents.add(frozenset(new_clause))

    return resolvents


def resolution(KB, query):
    # Negate the query and add it to KB
    clauses = set(frozenset(c) for c in KB)
    clauses.add(frozenset({"~" + query}))

    print("Initial Clauses:")
    for clause in clauses:
        print(clause)

    while True:
        new_clauses = set()

        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):

                resolvents = resolve(
                    set(clause_list[i]),
                    set(clause_list[j])
                )

                for resolvent in resolvents:

                    # Empty clause indicates contradiction
                    if len(resolvent) == 0:
                        print("\nEmpty clause {} derived.")
                        return True

                    new_clauses.add(resolvent)

        if new_clauses.issubset(clauses):
            return False

        clauses.update(new_clauses)


# Execute resolution
print("\nApplying Resolution:")

if resolution(KB, query):
    print("\nQuery is PROVED using Resolution.")
else:
    print("\nQuery cannot be proved using Resolution.")
