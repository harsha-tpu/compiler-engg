# Define grammar
grammar = {
    'X': [['A', 'B', 'C']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['c'], ['d']]
}

terminals = ['a', 'b', 'c', 'd']
non_terminals = list(grammar.keys())
first = {}
follow = {nt: set() for nt in non_terminals}

# FIRST computation
def first_of(symbol):
    if symbol in terminals:
        return {symbol}
    if symbol == 'ε':
        return {'ε'}
    if symbol in first:
        return first[symbol]

    result = set()
    for prod in grammar[symbol]:
        for sym in prod:
            sym_first = first_of(sym)
            result.update(sym_first - {'ε'})
            if 'ε' not in sym_first:
                break
        else:
            result.add('ε')
    first[symbol] = result
    return result

def first_of_string(symbols):
    if not symbols:
        return {'ε'}
    result = set()
    for sym in symbols:
        sym_first = first_of(sym)
        result.update(sym_first - {'ε'})
        if 'ε' not in sym_first:
            break
    else:
        result.add('ε')
    return result

# Compute FIRST sets
for nt in non_terminals:
    first_of(nt)

# FOLLOW computation
follow['X'].add('$')  # Start symbol

changed = True
while changed:
    changed = False
    for head in non_terminals:
        for prod in grammar[head]:
            trailer = follow[head].copy()
            for symbol in reversed(prod):
                if symbol in non_terminals:
                    if not trailer.issubset(follow[symbol]):
                        follow[symbol].update(trailer)
                        changed = True
                    if 'ε' in first[symbol]:
                        trailer = trailer.union(first[symbol] - {'ε'})
                    else:
                        trailer = first[symbol]
                else:
                    trailer = {symbol}

# Print FIRST sets
print("FIRST sets:")
for nt in non_terminals:
    print("FIRST(" + nt + ") =", first[nt])

# Print FOLLOW sets
print("\nFOLLOW sets:")
for nt in non_terminals:
    print("FOLLOW(" + nt + ") =", follow[nt])

