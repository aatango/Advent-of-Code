#include <fstream>
#include <iostream>
#include <string>

#include <vector>

/* Supply stacks
 *
 * PREPARE THE INPUTS:
 * 1. Cut the header into the vector of vectors below; and
 * 2. remove the text from the instruction list.
 *
 * This puzzle doesn't work properly with the aoc.sh;
 * the appropriate structure needs to be passed as parameter
 * both here in the source code (in main), and to aoc.sh.
 */

[[maybe_unused]] std::vector<std::vector<char>> starting_ex{
	{'Z', 'N'}, {'M', 'C', 'D'}, {'P'}
};

[[maybe_unused]] std::vector<std::vector<char>> starting_input{
	{'J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'},
	{'V', 'W', 'J'},
	{'G', 'V', 'L', 'J', 'B', 'T', 'H'},
	{'B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'},
	{'F', 'W', 'S', 'M', 'P', 'R', 'G'},
	{'G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'},
	{'D', 'H', 'G', 'M', 'R'},
	{'H', 'N', 'M', 'V', 'Z', 'D'},
	{'G', 'N', 'F', 'H'}
};

std::string  solveDay5(char const *p, auto stacks) {
	std::string top_crates{};

	std::ifstream i{p};
	for(unsigned count{}, start{}, end{};
	i >> count >> start >> end; ) {
		for (unsigned u{0}; u < count; ++u) {
			char crate{stacks.at(start - 1).back()};
			stacks.at(start - 1).pop_back();
			stacks.at(end - 1).push_back(crate);
		}
	}
	for (auto stack : stacks) {
		top_crates.push_back(stack.back());
	}

	return top_crates;
}

auto print = [](std::vector<char> v) {
	for(auto c : v) {
		std::cout << c << ' ';
	}
	std::cout << std::endl;
};
std::string  solveDay5b(char const *p, auto stacks) {
	std::string top_crates{};

	std::ifstream i{p};
	for(unsigned count{}, start{}, end{};
	i >> count >> start >> end; ) {
		std::vector<char> &moved_stack{stacks.at(start - 1)};
		std::vector<char> crates{
			moved_stack.end() - count,
			moved_stack.end()
		};
		moved_stack.erase(
			moved_stack.end() - count,
			moved_stack.end()
			);
		stacks.at(end - 1).insert(
			stacks.at(end - 1).end(),
			crates.begin(), crates.end()
			);
	}
	for (auto stack : stacks) {
		top_crates.push_back(stack.back());
	}

	return top_crates;
}
int main(int, char **argv) {
	std::cout << "Pt1: " << solveDay5(argv[1], starting_input) << std::endl;
	std::cout << "Pt2: " << solveDay5b(argv[1], starting_input) << std::endl;
}

