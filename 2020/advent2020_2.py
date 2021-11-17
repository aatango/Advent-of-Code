def main(input):
	"""
	"""

	valid_password = 0

	for i in input:
		limit, char, password = i.split(" ")

		char_count = password.count(char[0])
		min, max = limit.split("-")

		if char_count >= int(min) and char_count <= int(max):
			valid_password += 1

	return valid_password


def extra(input):
	"""
	"""

	valid_password = 0

	for i in input:
		limit, char, password = i.split()
		min, max = limit.split("-")

		if (password[int(min) - 1] == char[0]) ^ (password[int(max) - 1] == char[0]):
			valid_password += 1

	return valid_password


if __name__ == "__main__":
	with open("../../input", "r") as file:
		input = file.readlines()

	print("main: ", main(input))
	print("extra: ", extra(input))

