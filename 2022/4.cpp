#include <fstream>
#include <iostream>
#include <string>

#include <numeric>
#include <algorithm>
#include <vector>
#include <ranges>

/* Rucksack Reorganisation
 * Remove dashes, and commas from the input before solving the puzzle.
 * Ex; 2-4,6-8	->	2 4 6 8
 * This is to avoid having to handle these characters in C++.
 */

unsigned  solveDay4(char const *p) {
	unsigned fully_contained{0};

	std::ifstream i{p};
	for (unsigned first_start{}, first_end{}, second_start{}, second_end{};
	i >> first_start >> first_end >> second_start >> second_end; ) {
		std::vector<unsigned> first(first_end - first_start + 1);
		std::iota(first.begin(), first.end(), first_start);

		std::vector<unsigned> second(second_end - second_start + 1);
		std::iota(second.begin(), second.end(), second_start);

		fully_contained += std::ranges::includes(first, second) ||
			std::ranges::includes(second, first);
	}
	return fully_contained;
}

unsigned  solveDay4b(char const *p) {
	unsigned fully_contained{};

	std::ifstream i{p};
	for (unsigned first_start{}, first_end{}, second_start{}, second_end{};
	i >> first_start >> first_end >> second_start >> second_end; ) {
		std::vector<unsigned> first(first_end - first_start + 1);
		std::iota(first.begin(), first.end(), first_start);

		std::vector<unsigned> second(second_end - second_start + 1);
		std::iota(second.begin(), second.end(), second_start);

		fully_contained += std::ranges::any_of(first, [second] (unsigned u)
			{
				return std::ranges::includes(second, std::vector<unsigned> {u});
			}
		);
	}
	return fully_contained;
}

int main(int, char **argv) {
	std::cout << "Pt1: " << solveDay4(argv[1]) << std::endl;
	std::cout << "Pt2: " << solveDay4b(argv[1]) << std::endl;
}

