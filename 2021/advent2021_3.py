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


def part_two(report: tuple[str]) -> int:
	"""What is the life support rating of the submarine?"""

	def triage(binaries: tuple[str], position: int, most_common: bool) -> tuple[str]:
		"""Returns tuple with binaries that have most/least common bit in the corresponding position."""

		# Find most common bit at position
		bit: int = 0
		for _, binary in enumerate(binaries):
			bit += int(binary[position])
		bit = bit / len(binaries)
		bit = round(bit) if bit != 0.5 else 1
		bit = int(not bit) if not most_common else bit

		# Triage binaries
		new_binaries: list = []
		for _, binary in enumerate(binaries):
			if int(binary[position]) == bit:
				new_binaries.append(binary)

		return tuple(new_binaries)

	oxygen_generator: tuple[str] = report
	co2_scrubber: tuple[str] = report

	for i, _  in enumerate(report[0]):
		oxygen_generator = triage(oxygen_generator, i, True)
		if len(oxygen_generator) == 1:
			break
	for i, _  in enumerate(report[0]):
		co2_scrubber = triage(co2_scrubber, i, False)
		if len(co2_scrubber) == 1:
			break

	# Be sure to represent your answer in decimal, not binary.
	return int(oxygen_generator[0], 2) * int(co2_scrubber[0], 2)


if __name__ == "__main__":
	with open("../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print(main(INPUT_FILE))
	print(part_two(INPUT_FILE))
