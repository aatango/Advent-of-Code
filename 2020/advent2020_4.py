class Passport:

	def __init__(self, input_string: str):
		self.fields = input_string.replace("\n", " ").split(" ")

		self.byr = self.__decode("byr")
		self.iyr = self.__decode("iyr")
		self.eyr = self.__decode("eyr")
		self.hgt = self.__decode("hgt")
		self.hcl = self.__decode("hcl")
		self.ecl = self.__decode("ecl")
		self.pid = self.__decode("pid")
		self.cid = self.__decode("cid")

	def __decode(self, field_input: str) -> str:
		""" Returns the value of each key in the passport, if any.

		Having to work on a list will make it slow, but for now it's fast enough.
		"""

		for field in self.fields:
			if field_input in field:
				return field[4:]

		return None

	def validate_birth_year(self) -> bool:
		if self.byr != None:
			return 1920 <= int(self.byr) <= 2002
		return False

	def validate_issue_year(self) -> bool:
		if self.iyr != None:
			return 2010 <= int(self.iyr) <= 2020
		return False

	def validate_expiration_year(self) -> bool:
		if self.eyr != None:
			return 2020 <= int(self.eyr) <= 2030
		return False

	def validate_height(self) -> bool:
		if self.hgt != None:
			unit = self.hgt[-2:]
			
			if unit == "cm":
				return 150 <= int(self.hgt[:-2]) <= 193
			elif unit == "in":
				return 59 <= int(self.hgt[:-2]) <= 76
		return False

	def validate_hair_color(self) -> bool:
		"""I know Regex exist, want to try without."""

		if self.hcl != None:
			if self.hcl[0] == "#":
				color = self.hcl[1:]

				if len(color) == 6:
					try:
						return bool(int(color, 16))
					except ValueError:
						pass
		return False

	def validate_eye_color(self) -> bool:
		colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		if self.ecl != None:
			if self.ecl in colors:
				return True
		return False

	def validate_passport_id(self) -> bool:
		if self.pid != None:
			return len(self.pid) == 9
		return False

	def validate_country_id(self) -> bool:
		""" A "serious" passport validation system would have something here.

		Since this field is to be ignored for the challenge, I won't bother.
		"""

		return self.cid != None

	def validate(self) -> bool:
		valid = \
			self.validate_birth_year() \
			and self.validate_issue_year() \
			and self.validate_expiration_year() \
			and self.validate_height() \
			and self.validate_hair_color() \
			and self.validate_eye_color() \
			and self.validate_passport_id() \
		#	and self.validate_country_id() \

		return valid


def main() -> None:
	valid_passports = 0
	
	for i in input_file:
		passport = Passport(i)
		if passport.validate():
			valid_passports += 1

	print(valid_passports)


if __name__ == "__main__":
	with open("../../input", "r") as file:
		input_file = file.read().split("\n\n")[:-1]

	main()

