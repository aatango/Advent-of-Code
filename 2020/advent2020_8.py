"""Advent of Code 2020, day 8"""

class Console:
	"""
	"""

	def __init__(self):
		self.accumulator = 0
		self.queued_instruction= 0
		self.instruction_set = set()

	def __check(self) -> bool:
		""" Checks if instruction was already run"""

		if self.queued_instruction not in self.instruction_set:
			self.instruction_set.add(self.queued_instruction)
			return True
		return False

	def acc(self, value: int) -> bool:
		""" Adds value to accumulator."""

		self.accumulator += value
		self.queued_instruction += 1
		return self.__check()

	def jmp (self, value: int) -> bool:
		""" Jumps to assinged instruction."""

		self.queued_instruction += value
		return self.__check()

	def nop (self, value) -> int:
		"""No OPeration."""

		self.queued_instruction += 1
		return self.__check()




def main() -> int:
	"""
	"""

	not_nintendo = Console()
	boot_console = True

	while boot_console:
		operation, argument = INPUT_FILE[not_nintendo.queued_instruction].split(" ")
		boot_console = getattr(not_nintendo, operation)(int(argument))

	return not_nintendo.accumulator


def extra():
	"""
	"""

	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

	print(main())
