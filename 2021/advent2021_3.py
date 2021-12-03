"""Advent of Code 2021, day 3: Binary Diagnostic"""

def main(report: tuple[str]) -> int:
	"""What is the power consumption of the submarine?

	(Be sure to represent your answer in decimal, not binary.)
	"""

	report_length = len(report)
	gamma_b = [0] * len(report[0])

	for i in range(len(gamma_b)):
		for line in report:
			gamma_b[i] += int(line[i])

		gamma_b[i] = round(gamma_b[i] / report_length)

	gamma_b = "".join(str(g) for g in gamma_b)

	gamma = int(gamma_b, 2)
	epsilon = (gamma ^ (2 ** (gamma.bit_length()) - 1))

	return gamma * epsilon


def part_two():
	"""
	"""
	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

	print(main(INPUT_FILE))
