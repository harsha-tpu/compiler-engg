from collections import OrderedDict, defaultdict

productions = OrderedDict()
non_terminals = []
n = int(input("enter no of non terminals: "))
for i in range(n):
    line = input().strip()
    parts = line.split("=")
    non_terminal = parts[0].strip()
    if non_terminal not in non_terminals:
        non_terminals.append(non_terminal)
    rules = parts[1].split("|")
    productions[non_terminal] = [rule.strip().split() for rule in rules]

terminals = set()
for rules in productions.values(): 
    for rule in rules: 
        for symbol in rule: 
            if symbol not in non_terminals and symbol != '#':
                terminals.add(symbol)
# calculating first
def first_of(symbol):
    if symbol in terminals: 
        return {symbol}
    if symbol == '#':
        return {'#'}
    if symbol in first and first[symbol]:
        return first[symbol]
    first_set = set() 
    for production in productions.get(symbol, []):
        for sym in production: 
            sym_first = first_of(sym)
            first_set.update(sym_first  -  {'#'})
            if '#' not in sym_first: 
                break
            else: 
                first_set.add('#')
    return first_set
# first starts here
first = defaultdict(set)
for nt in non_terminals: 
    first[nt] = first_of(nt)

# compute follow
follow = defaultdict(set)
start_symbol =  non_terminals[0]
follow[start_symbol].add('$')

updated = True
while updated:
    updated = False 
    for nt in non_terminals:
        for production in productions.get(nt, []):
            storage = follow[nt].copy()
            for symbol in reversed(production):
                if symbol in non_terminals: 
                    if not storage.issubset(follow[symbol]):
                        follow[symbol].update(storage)
                        updated = True
                    if '#' in first[symbol]:
                        storage = storage.union(first[symbol] - {'#'})
                    else: 
                        storage = first[symbol]
                else: 
                    storage = {symbol}

def first_of_string(symbols):
    if not symbols: 
        return {'#'}
    result = set()
    for symbol in symbols: 
        sym_first = first_of(symbol)
        result.update(sym_first - {'#'})
        if '#' not in sym_first:
            break
        else: 
            result.add('#')
    return result

# constructing parse table
parse_table = defaultdict(dict)
for nt in non_terminals:
    for production in productions[nt]:
        first_production = first_of_string(production)
        for terminal in first_production - {'#'}:
            parse_table[nt][terminal] = production
        if '#' in first_production:
            for terminal in follow[nt]:
                parse_table[nt][terminal] = production

# display parse table here

# for string checking 
string = input("Enter a string to check: ")
tokens = string.strip().split() + ['$']
stack = ['$']
stack.append(non_terminals[0])
index = 0
while stack: 
    cur_stack = "".join(stack[::-1])
    remain_inp = "".join(tokens[index:])
    top = stack.pop()
    if top in  terminals or top == '$':
        if top == tokens[index]: 
            # match found 
            index += 1
        else: 
            # not match error
            print('error')
            break
    else: 
        token = tokens[index]
        production = parse_table.get(top, {}).get(token)
        if production is None: 
            print('error') 
            break
        else: 
            if production != ['#']:
                for symbol in reversed(production):
                    stack.append(symbol)
    if top == '$' and tokens[index] == '$':
        print('string parsed success') 
        break      