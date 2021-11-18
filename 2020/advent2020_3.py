def main(input: list[str], right: int, down: int) -> int:
	"""How many trees would encounter through path.

	Travels {right} and {down} each time.
	Finding the modulus of the position, allows to mimic an infinitely
	repeating string (which represents the local geography)

	ARGS:
		right	how many steps to the right to take
		down	steps down per iteration

	RETURNS
		trees	how many trees where found along the path
	"""

	step, trees = 0, 0
	path = input[down::down]
	street_length = len(input[0]) - 1	# Starts at index 0

	for street in path:
		step += 1
		position = (step * right) % street_length
		if street[position] == "#":
			trees += 1

	return trees


if __name__ == "__main__":
	with open("../../input", "r") as file:
		input = file.readlines()

	print(main(input, 3, 1))
	print(
		"Part two: ",
		main(input, 1, 1) *\
		main(input, 3, 1) *\
		main(input, 5, 1) *\
		main(input, 7, 1) *\
		main(input, 1, 2)
	)

	
