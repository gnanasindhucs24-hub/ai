
def is_variable(x):
    """A variable starts with a lowercase letter."""
    return isinstance(x, str) and x[0].islower()


def occurs_check(var, expr, subst):
    """Check whether variable occurs in expression."""
    expr = substitute(expr, subst)

    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs_check(var, arg, subst) for arg in expr[1:])

    return False


def substitute(expr, subst):
    """Apply substitutions recursively."""
    if isinstance(expr, str):
        while expr in subst:
            expr = subst[expr]
        return expr

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            substitute(arg, subst) for arg in expr[1:]
        )

    return expr


def unify_var(var, x, subst):
    """Unify a variable with another expression."""

    if var in subst:
        return unify(subst[var], x, subst)

    if isinstance(x, str) and x in subst:
        return unify(var, subst[x], subst)

    if occurs_check(var, x, subst):
        return None

    subst[var] = x
    return subst


def unify(x, y, subst=None):
    """Find the Most General Unifier (MGU)."""

    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        return unify_var(x, y, subst)

    if is_variable(y):
        return unify_var(y, x, subst)

    if isinstance(x, tuple) and isinstance(y, tuple):

        # Function/predicate names must match
        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    return None


# Example 1
expr1 = ("P", "x", "a")
expr2 = ("P", "b", "y")

result = unify(expr1, expr2)

print("Expression 1:", expr1)
print("Expression 2:", expr2)
print("MGU:", result)


# Example 2: Nested functions
expr3 = ("P", ("f", "x"), "y")
expr4 = ("P", ("f", "a"), "b")

result = unify(expr3, expr4)

print("\nNested expression MGU:", result)


# Example 3: Unification failure
expr5 = ("P", "x", "x")
expr6 = ("P", "a", "b")

result = unify(expr5, expr6)

print("\nUnification result:", result)
