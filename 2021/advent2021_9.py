"""Advent of Code 2021, day 9: Smoke Basin"""

def main(input_matrix: tuple[str]) -> int:
	"""
	Find all of the low points on your heightmap.
	What is the sum of the risk levels of all low points on your heightmap?
	"""

	# It's a brute force approach that does not scale to part two,
	# but it's what I could think of with very little time.

	# Transform string input into usable int values.
	for line in input_matrix:
		int_line: list[int] = []
		for num in line:
			int_line.append(int(num))
		DEPTH_MAP.append(int_line)

	# Find local minima.
	low_points: list[int] = []
	for line_index, line in enumerate(DEPTH_MAP):
		for point_index, point in enumerate(line):

			neighbours: list[int] = []
			if point_index - 1 in range(0, len(line)):
				neighbours.append(DEPTH_MAP[line_index][point_index - 1])

			if point_index + 1 in range(0, len(line)):
				neighbours.append(DEPTH_MAP[line_index][point_index + 1])

			if line_index - 1 in range(0, len(DEPTH_MAP)):
				neighbours.append(DEPTH_MAP[line_index - 1][point_index])

			if line_index + 1 in range(0, len(DEPTH_MAP)):
				neighbours.append(DEPTH_MAP[line_index + 1][point_index])

			if point < min(neighbours):
				low_points.append(point + 1)


	return sum(low_points)


def part_two():
	"""What do you get if you multiply together the sizes of the three largest basins?

	Unlike most other days, this part_two() is dependent on main(),
	as it's there that the global DEPTH_MAP is generated.
	"""

	def map_basin(pos: tuple[int], basin_size: int = 0) -> int:
		if DEPTH_MAP[pos[0]][pos[1]] >= 9:
			return basin_size

		basin_size += 1
		DEPTH_MAP[pos[0]][pos[1]] = 9

		basin_size += map_basin((max(pos[0] - 1, 0), pos[1]))
		basin_size += map_basin((min(pos[0] + 1, len(DEPTH_MAP) - 1), pos[1]))
		basin_size += map_basin((pos[0], max(pos[1] - 1, 0)))
		basin_size += map_basin((pos[0], min(pos[1] + 1, len(DEPTH_MAP[0]) - 1)))

		return basin_size


	basins_sizes: list[int] = []

	# This loop is to initiate recursive calls, whenever it finds a new basin.
	for line_index, line in enumerate(DEPTH_MAP):
		for point_index, point in enumerate(line):
			if point < 9:
				basins_sizes.append(map_basin((line_index, point_index)))

	basins_sizes.sort()

	return basins_sizes[-3] * basins_sizes[-2] * basins_sizes[-1]


if __name__ == "__main__":
	with open("../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	# Global so that it doesn't have to be remade for part two.
	DEPTH_MAP: list[list[int]] = []

	print(main(INPUT_FILE))
	print(part_two())
