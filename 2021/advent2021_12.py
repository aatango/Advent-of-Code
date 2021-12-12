"""Advent of Code 2021, day 12: Passage Pathing

The current method, can reach the maximum recursion depth, without finishing;
in this case, an error is returned!
"""

def parse_input() -> dict[str, list[str]]:
	"""Parses input into usable format.

	Generates a graph through an adjacency list;
	the graph being mostly undirected, "start" and "end" are directed nodes though:
	a path can never finish at start, nor can it begin at end.
	"""

	parsed_input: dict[str, list[str]] = {}

	with open("../../input", "r") as file:
		input_file = file.read().splitlines()

	# filter input to adjacency list
	for line in input_file:
		start, end = line.split("-")
		if start not in parsed_input:
			parsed_input[start] = []
		if "start" != end:
			parsed_input[start].append(end)
		if "start" != start and end != "end":
			if end not in parsed_input:
				parsed_input[end] = []
			parsed_input[end].append(start)

	return parsed_input


def find_path(graph: dict[str, list[str]], start: str, end: str) -> bool:
	"""Attempts to find a path between start and end points, using available graph."""
	raise NotImplementedError


def part_one(graph: dict[str, list[str]], start: str = "start", end: str = "end", ans: int = 0) -> int:
	"""How many paths through this cave system are there that visit small caves at most once?

	If 1st char is lowercase then it can only be passed through once;
	to make this happen, delete key value once node has been visited.
	Else, if 1st char is upper case, do not delete key, as this node can be visited multiple times.
	"""

	try:
		starts: list[str] = graph[start]
	except KeyError:
		return ans

	if start.islower() and start != "start":
		graph.pop(start)

	for node in starts:
		if node == end:
			ans += 1
		else:
			# dict(graph) to create a new graph, not use the same reference.
			ans = part_one(dict(graph), node, end, ans)

	return ans


def part_two():
	"""
	"""
	raise NotImplementedError


if __name__ == "__main__":
	input_data = parse_input()

	print("1: ", part_one(input_data))
	#print("2: ", part_two())
