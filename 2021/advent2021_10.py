"""Advent of Code 2021, day 10: Syntax Scoring

Both parts are executed through main().
"""

def main() -> tuple:
	"""main: What is the total syntax error score for those errors?
	part two: What is the middle autocompletion score?
	"""

	chunk_table: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}

	# scoring main problem
	score_error: int = 0
	scoring_error: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}

	# scoring part two
	score_completion: list[int] = []
	scoring_completion: dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}

	for line in INPUT_FILE:
		char_stack: list[str] = []

		# main
		for char in line:
			if char in chunk_table:
				char_stack.append(char)
			else:
				if char != chunk_table[char_stack[-1]]:
					score_error += scoring_error[char]
					break
				else:
					char_stack.pop()

		# part two
		else:
			score: int = 0
			for char in reversed(char_stack):
				score *= 5
				score += scoring_completion[chunk_table[char]]
			score_completion.append(score)

	score_completion.sort()

	return score_error, score_completion[len(score_completion) // 2]


if __name__ == "__main__":
	with open("../input", "r") as file:
		INPUT_FILE = tuple(file.read().splitlines())

	print(main())
