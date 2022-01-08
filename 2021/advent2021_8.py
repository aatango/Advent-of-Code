"""Advent of Code 2021, day 8: Seven Segment Search

Method used for part one will not work for part two.
"""

def main(input_stream: tuple[str]) -> int:
	"""In the output values, how many times do digits 1, 4, 7, or 8 appear?"""

	counter: int = 0

	for stream in input_stream:
		_, _, output_pattern = stream.partition("|")
		output_pattern = output_pattern.split()

		for pattern in output_pattern:
			if (
				len(pattern) == 2 or\
				len(pattern) == 4 or\
				len(pattern) == 3 or\
				len(pattern) == 7
			):
				counter += 1

	return counter


def part_two(notes: tuple[str]) -> int:
	"""What do you get if you add up all of the output values?"""

	notes_value: int = 0

	for note in notes:
		decoded_pattern: list[set[str]] = [None] * 10

		signal_pattern, _, output_pattern = note.partition("|")

		# Decode scrambled segment mapping.
		signal_pattern = signal_pattern.split()
		signal_pattern.sort(key=lambda i: len(i))

		decoded_pattern[1] = set(signal_pattern[0])
		decoded_pattern[7] = set(signal_pattern[1])
		decoded_pattern[4] = set(signal_pattern[2])
		decoded_pattern[8] = set(signal_pattern[9])

		# 6 characters/wires long signals
		for signal in signal_pattern[6: 9]:
			signal_set: set[str] = set(signal)
			if not decoded_pattern[7].issubset(signal_set):
				decoded_pattern[6] = signal_set
			elif decoded_pattern[4].issubset(signal_set):
				decoded_pattern[9] = signal_set
			else:
				decoded_pattern[0] = signal_set

		# 5 characters/wires long signals
		for signal in signal_pattern[3: 6]:
			signal_set: set[str] = set(signal)

			if decoded_pattern[1].issubset(signal_set):
				decoded_pattern[3] = signal_set
			elif signal_set.issubset(decoded_pattern[6]):
				decoded_pattern[5] = signal_set
			else:
				decoded_pattern[2] = signal_set

		# Find output numbers
		output_pattern = output_pattern.split()
		note_value: str = ""

		for output_signal in output_pattern:
			for i, decoded_signal in enumerate(decoded_pattern):
				if decoded_signal == set(output_signal):
					note_value += str(i)

		notes_value += int(note_value)

	return notes_value


if __name__ == "__main__":
	with open("../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print(main(INPUT_FILE))
	print(part_two(INPUT_FILE))
