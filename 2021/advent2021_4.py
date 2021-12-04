"""Advent of Code 2021, day 4: Giant Squid

main() and part_two() share a lot of identical code;
sending it through a parsing function, or using global variables,
was deemed unecessary for the purposes of this challenge.
"""

class BingoBoard:
	"""
	Drawn items are represented by negative number in the board;
	since numbers are a maximum of two digits, -100 will always be smaller.
	"""

	def __init__(self, board_layout: list[int]):
		self.board: list[int] = board_layout
		self.drawn_number: int = 0
		self.score: int = 0
		self.grid_size: tuple(int) = 5, 5
		self.reducer: int = -100

	def __bingo_row(self, index: int) -> bool:
		"""Checks if row where number was drawn wins the game."""

		row_number = index // self.grid_size[1]
		row = self.board[row_number * self.grid_size[1] : (1 + row_number) * self.grid_size[1]]

		for elem in row:
			if elem >= 0:
				return False

		self.__tally_score()

		return True

	def __bingo_column(self, index: int) -> bool:
		"""Checks if column where number was drawn wins the game."""

		column_number = index % self.grid_size[1]
		column = self.board[
			column_number : column_number + self.grid_size[1] * self.grid_size[0] : self.grid_size[1]
		]

		for elem in column:
			if elem >= 0:
				return False

		self.__tally_score()

		return True

	def __tally_score(self) -> None:
		"""Once victory is achieved, calculates the score."""

		self.score = sum([elem for elem in self.board if elem >= 0]) * self.drawn_number

	def draw(self, number: int) -> bool:
		"""Checks if number is in board, and initiates win conditions."""

		self.drawn_number = number

		if self.drawn_number in self.board:
			index = self.board.index(self.drawn_number)
			self.board[index] += self.reducer
			if self.__bingo_column(index) or self.__bingo_row(index):
				return True

		return False


def iterate_boards(drawing_orders: list[int], boards: list[object], count: int = 1) -> int:
	"""Plays through the available boards and returns the score."""

	for i, order in enumerate(drawing_orders):
		for board in boards:
			if board.draw(order):  # True if latest draw wins the game
				if count == 1:
					return board.score
				boards.remove(board)
				return iterate_boards(drawing_orders[i:], boards, len(boards))

	return -1


def main(input_stream: str) -> int:
	"""To guarantee victory against the giant squid, figure out which board will win first.

	What will your final score be if you choose that board?
	"""


	drawing_orders: list[int] = [
		int(elem) for elem in input_stream.split("\n\n")[0].split(",")
	]
	boards: list[object] = []

	for board in input_stream.split("\n\n")[1:]:
		converted_board = [int(elem) for elem in board.replace("\n", " ").split()]
		boards.append(BingoBoard(converted_board))

	return iterate_boards(drawing_orders, boards)


def part_two(input_stream: str) -> int:
	"""Figure out which board will win last. Once it wins, what would its final score be?"""

	drawing_orders: list[int] = [
		int(elem) for elem in input_stream.split("\n\n")[0].split(",")
	]
	boards: list[object] = []

	for board in input_stream.split("\n\n")[1:]:
		converted_board = [int(elem) for elem in board.replace("\n", " ").split()]
		boards.append(BingoBoard(converted_board))

	return iterate_boards(drawing_orders, boards, len(boards))

if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read()

	print(main(INPUT_FILE))
	print(part_two(INPUT_FILE))
