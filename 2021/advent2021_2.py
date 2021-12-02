"""Advent of Code 2021, day 2: Dive!"""

def main(instructions: tuple[str]) -> int:
	"""What do you get if you multiply your final horizontal position by your final depth?

	up/down change depth; forward changes position.
	"""

	depth = 0
	position = 0

	for instruction in instructions:
		direction, magnitude = instruction.split()
		magnitude = int(magnitude)

		if direction == "forward":
			position += magnitude
		elif direction == "down":
			depth += magnitude
		elif direction == "up":
			depth -= magnitude

	return depth * position


def part_two(instructions: tuple[str]) -> int:
	"""What do you get if you multiply your final horizontal position by your final depth?

	up/down change aim; forward changes both position and depth.
	"""

	aim = 0
	depth = 0
	position = 0

	for instruction in instructions:
		direction, magnitude = instruction.split()
		magnitude = int(magnitude)

		if direction == "forward":
			position += magnitude
			depth += magnitude * aim
		elif direction == "down":
			aim += magnitude
		elif direction == "up":
			aim -= magnitude

	return depth * position


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print(main(INPUT_FILE))
	print(part_two(INPUT_FILE))
