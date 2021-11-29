"""Advent of Code 2020, Day 12: Rain Risk"""

import math

class Ferry:
	"""This is a ferry!

	Its heading is given in polar coordinates; and position in cartesian coordinates.
	"""

	def __init__(self):
		self.heading = 0	# angle in degrees
		self.position = (0, 0)
		self.waypoint = (10, 1)

	def move(self, movement: int, direction: int) -> None:
		"""Moves the ferry along a certain heading.

		ARGS:
			movement: int - how much to move.
			direction: int - heading along wich to move.
		"""

		current_position = self.position
		rad = math.radians(direction)

		self.position = (
			current_position[0] + movement * math.cos(rad),
			current_position[1] + movement * math.sin(rad),
		)

	def rotate(self, deg: int, orientation: int) -> None:
		"""Rotates the ferry by given degrees; positives are counter-clockwise."""

		relative_orientations = {"L": 1, "R": -1}

		self.heading = self.heading + relative_orientations[orientation] * deg
		


def main():
	"""What is the Manhattan distance between that location and the ship's starting position?

	Where given instructions indicate movement and heading of ship.
	"""

	ferry = Ferry()
	directions = tuple(INPUT_FILE)

	cardinal_directions = {
		"N": 90,
		"W": 180,
		"S": -90,
		"E": 0,
	}

	for direction in directions:
		instruction = direction[0]
		magnitude = int(direction[1:])

		if instruction == "F":
			ferry.move(magnitude, ferry.heading)
		elif instruction in ("N", "W", "S", "E"):
			ferry.move(magnitude, cardinal_directions[instruction])
		else:
			ferry.rotate(magnitude, instruction)

	return abs(ferry.position[0]) + abs(ferry.position[1])

def part_two():
	"""What is the Manhattan distance between that location and the ship's starting position?

	Where instructioins are relative to the ship's waypoint.
	"""
	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

	print(main())
