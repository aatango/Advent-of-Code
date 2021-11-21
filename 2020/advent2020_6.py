"""Advent of Code 2020, day 6"""

def main() -> int:
	""" Custom Customs."""

	plane_yesses = 0

	for line in INPUT_FILE:
		form = set(line.replace("\n", ""))
		plane_yesses += len(form)

	return plane_yesses


def extra() -> int:
	""" Part two ..."""

	plane_yes = 0

	for line in INPUT_FILE:
		form = [set(s) for s in line.split("\n")]
		plane_yes += len(form[0].intersection(*form[1:]))

	return plane_yes


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().split("\n\n")[:-1]

	print("Day 6:", main())
	print("Extra:", extra())
