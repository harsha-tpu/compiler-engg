# local list scheduling
from collections import Counter, defaultdict, deque
from heapq import *

delay = {}
print('Enter nodes with latencies: ')
while True: 
	line = input().strip()
	if not line: 
		break
	i, d = line.split()
	delay[i] = int(d)
	
successors = defaultdict(list)
predecessors = defaultdict(list)
in_degree = Counter()
out_degree = Counter()

print('Enter the dependencies: ')
while True: 
	line = input().strip()
	if not line: 
		break
	u, v = line.split()
	successors[u].append(v)
	predecessors[v].append(u)
	in_degree[v] += 1
	out_degree[u] += 1
	
priority = Counter() 
queue = deque([i for i in delay if out_degree[i] == 0])

# finding priority
while queue: 
	node = queue.popleft()
	priority[node] = max(priority[node], delay[node])
	for p in predecessors[node]: 
		priority[p] = max(priority[p], priority[node] + delay[p])
		out_degree[p] -= 1
		if out_degree[p] == 0: 
			queue.append(p)
			
# scheduling part 
# elements here don't have dependencies
ready = [(-priority[i], i) for i in delay if in_degree[i] == 0]
heapify(ready)
active = []
cycle = 1

print('----Scheduling Trace----')
while ready or active: 
	finished = []
	for start, i in active: 
	# check if finished and add it's dependent to ready
		if start + delay[i] == cycle: 
			finished.append(i)
			for s in successors[i]: 
				in_degree[s] -= 1 
				if in_degree[s] == 0: 
					heappush(ready, (-priority[s], s))
					
	# refresh active list
	active = [(start, i) for start, i in active if i not in finished]
	
	# if finished is empty
	if ready: 
		prio, i = heappop(ready)
		active.append((cycle, i))
		
	cycle += 1
	
print('Total number of cycles', cycle - 1)


