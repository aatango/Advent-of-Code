"""
Advent of code 2020

Day 7: Handy Haversacks
"""

import re

def parse_input() -> dict:
	""" Parses input file into a dictionary
	"""

	parsed_rules ={}

	for line in INPUT_FILE:
		container, contained = line.split(" bags contain")
		if "no other" in contained:
			contained = []
		else:
			contained = [s.split(" ", 1) for s in re.findall("\d*[a-z\s]+(?= bag)", contained)]
		parsed_rules[container.strip()] = contained

	return parsed_rules


def search_recursively(bag_rules: dict, bag_target: str, bag_key: str) -> int:
	"""
	"""

	contained = bag_rules[bag_key]
	if len(contained) == 0:
		return 0
	for rule in contained:
		if bag_target in rule[1]:
			return 1
		return search_recursively(bag_rules, bag_target, rule[1])


def main(bag_rules: dict, my_bag: str) -> int:
	""" Split strings into a dictionary. Container bags: contained bags.

	Split values into 2d arrays, (how many bags, and of what color).
	For each value, iterate through keys to find if bag exists.
	Recursive calls until bag contains no other.
	"""

	count = 0
	for contains in bag_rules.keys():
		count += search_recursively(bag_rules, my_bag, contains)

	return count


def extra():
	"""
	"""

	raise NotImplementedError


if __name__ == "__main__":
	with open("../../input", "r") as file:
		INPUT_FILE = file.read().splitlines()

	print("Day 7:", main(parse_input(), "shiny gold"))
#	print("Extra:", extra())
