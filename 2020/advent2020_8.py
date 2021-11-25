"""Advent of Code 2020, day 8"""

class Handheld:
	"""Handheld gaming console."""

	def __init__(self):
		self.accumulator = 0
		self.queued_address = 0
		self.executed_addresses = set()

	def __check(self) -> bool:
		"""Checks if instruction was already run."""

		if self.queued_address not in self.executed_addresses and self.queued_address >= 0:
			self.executed_addresses.add(self.queued_address)

			return True

		return False

	def boot(self, boot_sequence: list[str]) -> bool:
		"""Attempts to boot the handheld.

		Detects infinite loop, and breaks boot sequence.
		"""

		boot_status = True

		while boot_status:
			if self.queued_address >= len(boot_sequence):
				return True

			operation, argument = boot_sequence[self.queued_address].split()

			if operation == "acc":
				self.accumulator += int(argument)
				self.queued_address += 1

			elif operation == "jmp":
				self.queued_address += int(argument)

			elif operation == "nop":
				self.queued_address += 1

			boot_status = self.__check()

		return False


def main() -> int:
	"""Attempt to boot handheld without changing the boot sequence."""

	not_nintendo = Handheld()

	not_nintendo.boot(INPUT_FILE)
	return not_nintendo.accumulator


def extra() -> int:
	"""Fixes original boot error, and returns accumulator value at end of sequence."""

	for i, instruction in enumerate(INPUT_FILE):
		not_nintendo = Handheld()
		instruction_list = INPUT_FILE[:]
		if "nop" in instruction:
			instruction_list[i] = "jmp" + instruction[3:]
		elif "jmp" in instruction:
			instruction_list[i] = "nop" + instruction[3:]
		if not_nintendo.boot(instruction_list):
			return not_nintendo.accumulator

	return 0


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

#	print(main())
	print(extra())
