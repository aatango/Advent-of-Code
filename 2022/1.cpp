#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>


unsigned solveDay1(unsigned top_elves) {
	std::ifstream i{"./1.input"};
	unsigned calories_carried{0};
	std::vector<unsigned> calories_per_elf{0};

	for (std::string line; getline(i, line); ){
		if (!line.empty()) {
			calories_carried += std::stoi(line);
		} else {
			calories_per_elf.push_back(calories_carried);
			calories_carried = 0;
		}
	}

	std::sort(
		calories_per_elf.begin(),
		calories_per_elf.end(),
		std::greater<unsigned>()
	);

	return std::accumulate(
		calories_per_elf.begin(),
		calories_per_elf.begin() + top_elves,
		0
	);
}

// Calorie Counting
int main() {
	std::cout << "Pt1: " << solveDay1(1) << std::endl;
	std::cout << "Pt2: " << solveDay1(3) << std::endl;
}
