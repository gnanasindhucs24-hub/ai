facts = [
    ("Human", "John"),
    ("Human", "Mary")
]


rules = [
    ("Human", "Mortal"),
    ("Mortal", "Living")
]


query = ("Living", "John")

def forward_chaining(facts, rules, query):

    print("Initial Facts:")
    for fact in facts:
        print(fact)

    new_fact_added = True

    while new_fact_added:
        new_fact_added = False

        for condition, conclusion in rules:
            for fact in facts[:]:

                if fact[0] == condition:

                    new_fact = (conclusion, fact[1])

                
                    if new_fact not in facts:
                        facts.append(new_fact)
                        new_fact_added = True
                        print("New Fact Derived:", new_fact)

    print("\nFinal Knowledge Base:")
    for fact in facts:
        print(fact)

    if query in facts:
        print("\nQuery:", query)
        print("Query is PROVED.")
    else:
        print("\nQuery:", query)
        print("Query cannot be proved.")


forward_chaining(facts, rules, query)




