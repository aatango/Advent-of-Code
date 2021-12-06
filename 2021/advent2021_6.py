"""Advent of Code 2021, day 6: Lanternfish

Trying to simulate every single fish will take too much space and/or time;
the solution to this is: Dynamic programing with memoisation!

Parts of spawn() are also in main(), which leads me to think I could optimise the code,
but I've already took long enough to get here, and the solution works fine, and fast.
"""

def spawn(school: list[int], cycles: int, memo: dict[int, int]):
	"""Simulates fish reproduction when not already stored."""

	school_size: int = len(school)

	for fish in school:
		if fish not in memo:
			spawned_fish: list[int] = []
			day: int = fish
			day += 9
			while day <= cycles:
				spawned_fish.append(day)
				day += 7
			memo[fish], memo = spawn(spawned_fish, cycles, memo)
		school_size += memo[fish]

	return school_size, memo


def main(cycles: int = 80):
	"""Find a way to simulate lanternfish. How many lanternfish would there be after X days?"""

	school: list[int] = list(INPUT_FILE)
	school_size: int = len(school)

	memo: dict[int, int] = {}

	# initial school
	for fish in school:
		spawned_fish: list[int] = []
		day: int = fish + 1
		while day <= cycles:
			spawned_fish.append(day)
			day += 7
		new_school_size, memo = spawn(spawned_fish, cycles, memo)
		school_size += new_school_size

	return school_size


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = tuple(
			[int(value) for value in file.read()[:-1].split(",")]
		)

	print("Pt 1: ", main())
	print("Pt 2: ", main(256))
