#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as f:
	lines = list(map(int, f.readlines()))
	######## Part 1 ########
	#[199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

	#list(zip(lines, lines))
	#[(199, 199), (200, 200), (208, 208), (210, 210), (200, 200), (207, 207), (240, 240), (269, 269), (260, 260), (263, 263)]

	#list(zip(lines, lines[1:]))
	#[(199, 200), (200, 208), (208, 210), (210, 200), (200, 207), (207, 240), (240, 269), (269, 260), (260, 263)]


	part1 = sum([x0 < x1 for x0, x1 in zip(lines, lines[1:])])
	print(f"Part 1 = {part1}")

	######## Part 2 #########
	#[(lines[i:i+3], lines[i+1:i+4]) for i in range(len(lines)-2)]
	#[([199, 200, 208], [200, 208, 210]), ([200, 208, 210], [208, 210, 200]), ([208, 210, 200], [210, 200, 207]), ([210, 200, 207], [200, 207, 240]), ([200, 207, 240], [207, 240, 269]), ([207, 240, 269], [240, 269, 260]), ([240, 269, 260], [269, 260, 263]), ([269, 260, 263], [260, 263])]

	#[sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines)-2)]
	#[True, False, False, True, True, True, True, False]
	#part2 = sum([sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines)-2)])
	
	zipped = list(zip(lines, lines[1:], lines[2:]))
	#[(199, 200, 208), (200, 208, 210), (208, 210, 200), (210, 200, 207), (200, 207, 240), (207, 240, 269), (240, 269, 260), (269, 260, 263)]
	
	#list(zip(zipped, zipped[1:]))
	#[((199, 200, 208), (200, 208, 210)), ((200, 208, 210), (208, 210, 200)), ((208, 210, 200), (210, 200, 207)), ((210, 200, 207), (200, 207, 240)), ((200, 207, 240), (207, 240, 269)), ((207, 240, 269), (240, 269, 260)), ((240, 269, 260), (269, 260, 263))]

	part2 = sum([sum(x0) < sum(x1) for x0,x1 in list(zip(zipped, zipped[1:]))])

	print(f"Part 2: {part2}")

	##### generic solution ########
	def solve(*lists):
		zipped = list(zip(*lists))
		return sum([sum(x0) < sum(x1) for x0, x1 in zip(zipped, zipped[1:])])

	print(f"Part 1: {solve(lines)}")
	print(f"Part 2: {solve(lines, lines[1:], lines[2:])}")
