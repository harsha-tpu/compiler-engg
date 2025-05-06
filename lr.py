# getting input 

nut = int(input("no of terminals: "))
nunt = int(input("no of non terminals: "))

terminals = list()
print("enter the terminals: ")
for _ in range(nut): 
  terminals.append(input().strip())
  
non_terminals = list()
print("enter the non terminals: ")
for _ in range(nunt):
  non_terminals.append(input().strip())
  
symbols = terminals + non_terminals 

# parsing table here 


# grammar rules as dict 
grammar = {
  1: ('S': 'aAd'),
  2: 
}

# input str 
input_str = input("Enter input string (end with $): ").strip()
string = list(input_str)

# stack setup
stack = ['$', 0]
k = 0
flag = True

try: 
  while k < len(string):
    cur_symbol = string[k]
    state = int(stack[-1])
    
    if cur_symbol not in terminals:  
      raise ValueError(f"Invalid symbol in input: {cur_symbol}")
      
    col_index = symbols.index(cur_symbol)
    action = table[state][col_index]
    
    if action == 'accept': 
      print("accepted")
      break
    elif action.startswith('S'):
      # shift action
      stack.append(cur_symbol)
      stack.append(int(action[1:]))
      k += 1
    elif action.startswith('r'): 
      # reduce action
      rule_no = int(action[1:])
      lhs, rhs = grammar[rule_no]
      pop_len = 2 * len(rhs)
      for _ in range(pop_len):
        stack.pop()
      prev_state = int(stack[-1])
      stack.append(lhs)
      goto_index = symbols.index(lhs)
      next_state = table[prev_state][goto_index]
      if next_state == 'phi': 
        raise ValueError("Invalid goto transition")
      stack.append(int(next_state))
    else: 
      raise ValueError("invalid action from table")
    
    
except Exception as e: 
  flag = False
  print("not accepted")
  print(f"error: {e}")
