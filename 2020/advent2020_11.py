"""Advent of Code 2020, day 11: Seating System

Wanted to try and work with straight arrays.
Ended up going around in circles.
In the end, still works through a 1d array,
but I'm unclear how much of a pain it'll be to work with for part two.
"""

class SeatLayout:
	"""Seating arrangement on the ferry."""
	def __init__(self, input_list):
		self.row_count = input_list.count("\n")
		self.seats = input_list.replace("\n", "")
		self.row_length = len(self.seats) // self.row_count

	def __adjacency_list(self, seat_index: int) -> tuple:
		"""Returns all of the adjacent seats."""
		adjacent_seats = []

		# Index coordinates
		x = seat_index % self.row_length
		y = seat_index // self.row_length

		# Adjacent values
		x_min = max(0, x - 1)
		x_max = min(x + 1, self.row_length - 1)

		y_min = max(0, y - 1)
		y_max = min(y + 1, self.row_count - 1)

		for u in range(x_min, x_max + 1):
			for v in range(y_min, y_max + 1):
				w = u + v * self.row_length
				if w != seat_index:
					adjacent_seats.append(self.seats[w])

		return adjacent_seats

	def occupy_seat(self, seat_index: int) -> str:
		"""If there are no occupied seats adjacent to it, occupies the seat."""
		adjacent_seats = self.__adjacency_list(seat_index)

		if adjacent_seats.count("#") == 0:
			return "#"

		return self.seats[seat_index]

	def empty_seat(self, seat_index: int) -> str:
		"""If four or more seats adjacent to it are also occupied, the seat becomes empty."""
		adjacent_seats = self.__adjacency_list(seat_index)

		if adjacent_seats.count("#") >= 4:
			return "L"

		return self.seats[seat_index]


def main() -> int:
	"""
	Simulate your seating area by applying the seating rules repeatedly until no seats change state.
	How many seats end up occupied?
	"""

	ferry_seats = SeatLayout(INPUT_FILE)

	changed_seat = True

	while changed_seat:
		changed_seat = False
		new_seats = []

		for i, seat in enumerate(ferry_seats.seats):
			if seat == "#":
				seat = ferry_seats.empty_seat(i)
				if seat == "L":
					changed_seat = True
			elif seat == "L":
				seat = ferry_seats.occupy_seat(i)
				if seat == "#":
					changed_seat = True

			new_seats.append(seat)

		ferry_seats.seats = new_seats

	return ferry_seats.seats.count("#")


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read()

	print(main())
