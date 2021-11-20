"""Advent of Code 2020, day 5.
"""

def decode(search_input: str, post: str) -> int:
	""" Binary space partitioning.
	"""
	elem_length = 2 ** len(search_input)
	elem = 0

	for char in search_input:
		elem_length //= 2
		if char == post:
			elem += elem_length

	return elem


class BoardingPass:
	"""Defines a boarding pass, as described in the challenge's description.
	"""

	def __init__(self, puzzle_input):
		self.column = decode(puzzle_input[-3:], "R")
		self.row = decode(puzzle_input[:7], "B")
		self.seat_id = self.row * 8 + self.column


def main() -> int:
	""" Day5: Binary Boarding. """

	highest_id = 0

	for line in EXAMPLE_STRING:
		boarding_pass = BoardingPass(line)
		if boarding_pass.seat_id > highest_id:
			highest_id = boarding_pass.seat_id

	return highest_id


def extra() -> int:
	""" Part two ... """

	ids = set()

	for line in INPUT_FILE:
		boarding_pass = BoardingPass(line)
		ids.add(boarding_pass.seat_id)

	min_id = min(ids)
	max_id = max(ids)

	return set(range(min_id, max_id)) - ids


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE= file.read().splitlines()

	EXAMPLE_STRING= ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

	print("Day 5:", main())
	print("Extra:", extra())
