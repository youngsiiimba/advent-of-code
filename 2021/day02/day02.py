#!/usr/bin/env python3

import sys
import math

with open(sys.argv[1], 'r') as f:
	cmds = f.readlines()

####### Part 1 #######
pos, depth = 0, 0
for cmd in cmds:
	direction, qty = cmd.strip().split(" ")
	qty = int(qty)
	if direction == "forward":
		pos += qty
	elif direction == "down":
		depth += qty
	elif direction == "up":
		depth -= qty
	else: 
		import pdb;pdb.set_tract()
print(f"Part 1: {pos * depth}")	
	 

####### Part 2 #######
pos, depth, aim = 0, 0, 0
for cmd in cmds:
	direction, qty = cmd.strip().split(" ")
	qty = int(qty)
	if direction == "forward":
		pos += qty
		depth+=(aim*qty)
	elif direction == "down":
		aim += qty
	elif direction == "up":
		aim -= qty
	else:
		import pdb;pdb.set_tract()
print(f"Part 2: {pos * depth}")


####### Optimisation #########
def parse_line(line):
	direction, qty = line.strip().split(" ")
	qty = int(qty)
	if direction == "forward":
		return (qty, 0)
	if direction == "down":
		return (0, qty)
	if direction == "up":
		return (0, -qty)
	import pdb;pdp.set_tract()

###ignore###part1 = list(map(sum, (zip(*[parse_line(cmd) for cmd in cmds]))))
#part1 = math.prod(map(sum, (zip(*[parse_line(cmd) for cmd in cmds]))))
#print(f"Part 1(optimised code): {part1}")
