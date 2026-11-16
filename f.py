def convert_to_cnf():
    print("Original FOL Statement:")
    statement = "For all x: Human(x) -> Mortal(x)"
    print(statement)

    step1 = "~Human(x) OR Mortal(x)"
    print("\nAfter eliminating implication:")
    print(step1)

    step2 = "~Human(x) OR Mortal(x)"
    print("\nAfter moving negation inward:")
    print(step2)

    step3 = "~Human(x) OR Mortal(x)"
    print("\nAfter standardizing variables:")
    print(step3)

    step4 = "~Human(x) OR Mortal(x)"
    print("\nAfter Skolemization:")
    print(step4)

  
    step5 = "~Human(x) OR Mortal(x)"
    print("\nAfter removing universal quantifier:")
    print(step5)

  
    print("\nFinal CNF:")
    print("NOT Human(x) OR Mortal(x)")


convert_to_cnf()



