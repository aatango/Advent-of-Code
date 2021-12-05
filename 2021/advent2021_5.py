"""Advent of Code 2021, day 5: Hydrothermal Venture

Generating the proper grid took the vast majority of the required time.
Had some issues with avoiding shallow copies of lists.

Unclear if list of lists is appropriate data structure for such a grid.
"""

import re

def parse_input() -> dict[tuple[int], tuple[int]]:
	"""Helper function to parse input into usable data.

	Organises graph into directed adjacency list.
	"""

	lines: list[tuple[int], tuple[int]] = []

	rows: set[int] = set()
	columns: set[int] = set()

	for line in INPUT_FILE:
		coords: list[str] = re.split(r"\D+", line)

		start_pt: tuple[int] = int(coords[0]), int(coords[1])
		end_pt: tuple[int] = int(coords[2]), int(coords[3])
		lines.append((start_pt, end_pt))

		rows.add(int(coords[1]))
		rows.add(int(coords[3]))
		columns.add(int(coords[0]))
		columns.add(int(coords[2]))

	row_length: int = max(rows)
	column_length: int = max(columns)


	grid: list[list[int]] = list()

	for row_number in range(row_length + 1):
		row = list()
		for column_number in range(column_length + 1):
			row.append(0)
		grid.append(row)

	return lines, grid


def main() -> int:
	"""
	Consider only horizontal and vertical lines.
	At how many points do at least two lines overlap?
	"""

	l, g = parse_input()
	lines: dict[tuple[int], tuple[int]] = l
	grid: list[list[int]] = g

	for line in lines:
		if line[0][0] == line[1][0]:
			mini = min(line[0][1], line[1][1])
			maxi = max(line[0][1], line[1][1])

			for y in range(mini, maxi + 1):
				grid[y][line[0][0]] += 1

		elif line[0][1] == line[1][1]:
			mini = min(line[0][0], line[1][0])
			maxi = max(line[0][0], line[1][0])

			for x in range(mini, maxi + 1):
				grid[line[0][1]][x] += 1

	overlap: int = 0

	for column in grid:
		for cell in column:
			if cell >= 2:
				overlap += 1

	return overlap


def part_two():
	"""
	Consider all of the lines.
	At how many points do at least two lines overlap?
	"""

	l, g = parse_input()
	lines: dict[tuple[int], tuple[int]] = l
	grid: list[list[int]] = g

	for line in lines:
		miny = min(line[0][1], line[1][1])
		maxy = max(line[0][1], line[1][1])

		minx = min(line[0][0], line[1][0])
		maxx = max(line[0][0], line[1][0])

		if line[0][0] == line[1][0]:
			for y in range(miny, maxy + 1):
				grid[y][line[0][0]] += 1

		elif line[0][1] == line[1][1]:
			for x in range(minx, maxx + 1):
				grid[line[0][1]][x] += 1

		else:
			slope: int  = int((line[1][1] - line[0][1]) / (line[1][0] - line[0][0]))
			y_intercept: int = int(
				(line[1][0] * line[0][1] - line[0][0] * line[1][1]) / (line[1][0] - line[0][0])
			)

			for x in range(minx, maxx + 1):
				y = slope * x + y_intercept
				grid[y][x] += 1


	overlap: int = 0

	for column in grid:
		for cell in column:
			if cell >= 2:
				overlap += 1

	return overlap


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print(main())
	print(part_two())
