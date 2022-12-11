#include <fstream>
#include <iostream>
#include <string>

#include <set>

// Tuning Trouble
unsigned solveDay6(char const *p, unsigned unique_chars) {
	std::ifstream i{p};
	std::string signal{};
	i >> signal;

	for(unsigned s{unique_chars}; s < signal.size(); ++s) {
		std::set<char> set(signal.begin() + s - unique_chars, signal.begin() + s);
		if (set.size() == unique_chars) {
			return s;
		}
	}
	return 0;
};
int main(int, char **argv) {
	std::cout << "Pt1: " << solveDay6(argv[1], 4) << std::endl;
	std::cout << "Pt2: " << solveDay6(argv[1], 14) << std::endl;
}

