"""Advent of Code 2021, day 9: Smoke Basin

It's a brute force approach that does not scale to part two,
but it's what I could think of with very little time.
"""

def main(input_matrix: tuple[str]) -> int:
	"""
	Find all of the low points on your heightmap.
	What is the sum of the risk levels of all low points on your heightmap?
	"""

	# Transform string input into usable int values.
	depth_map: list[list[int]] = []
	for line in input_matrix:
		int_line: list[int] = []
		for num in line:
			int_line.append(int(num))
		depth_map.append(int_line)

	# Find local minima.
	low_points: list[int] = []
	for line_index, line in enumerate(depth_map):
		for point_index, point in enumerate(line):

			neighbours: list[int] = []
			if point_index - 1 in range(0, len(line)):
				neighbours.append(depth_map[line_index][point_index - 1])

			if point_index + 1 in range(0, len(line)):
				neighbours.append(depth_map[line_index][point_index + 1])

			if line_index - 1 in range(0, len(depth_map)):
				neighbours.append(depth_map[line_index - 1][point_index])

			if line_index + 1 in range(0, len(depth_map)):
				neighbours.append(depth_map[line_index + 1][point_index])

			if point < min(neighbours):
				low_points.append(point + 1)


	return sum(low_points)


def part_two():
	"""
	"""
	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print("1: ", main(INPUT_FILE))
