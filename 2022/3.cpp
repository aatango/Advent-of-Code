#include <fstream>
#include <iostream>
#include <string>


// Rucksack Reorganisation

unsigned  solveDay3(char const *p) {
	unsigned priority_sum{0};

	std::ifstream i{p};
	for (std::string line{}; i >> line; ){
		std::string first{ line.substr(0, line.size()/2) };
		std::string second{ line.substr(line.size()/2) };
		for (char c : first) {
			if (second.find(c) != std::string::npos) {
				priority_sum += c % 32;
				priority_sum += (c < 96 ? 26 : 0);
				break;
			}
		}
	}

	return priority_sum;
}

unsigned solveDay3b(char const *p) {
	unsigned priority_sum{0};

	std::ifstream i{p};
	for (std::string first{}, second{}, third{};
	     i >> first >> second >> third; ) {
		for(char c : first) {
			if (second.find(c) != std::string::npos &&
			    third.find(c) != std::string::npos) {
				    priority_sum += c % 32;
				    priority_sum += (c < 96 ? 26 : 0);
				    break;
			}
		}
	}

	return priority_sum;
}

int main(int, char **argv) {
	std::cout << "Pt1: " << solveDay3(argv[1]) << std::endl;
	std::cout << "Pt2: " << solveDay3b(argv[1]) << std::endl;
}
