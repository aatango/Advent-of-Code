#include <fstream>
#include <iostream>


/* Rock, Paper, Sissors: pt1
 *
 * This problem is solved using char manipulation,
 * and the difference of their unsigned values.
 *
 * I want to find a combination that returns:
 * 0 * 3 = 0 - loss
 * 1 * 3 = 3 - tie
 * 2 * 3 = 6 - win
 *
 * The relationship between the differences,
 * and the outcomes can be mapped as follows:
 *  W	 L	D	 W	 L
 * -2	-1	0	+1	+2
 *
 * From this map, we can achieve the combination above
 * by adding 4, and finding the remainder when divided by 3.
 *
 * As for the points for play,
 * simply calculate the difference to 87:
 * Rock		(X, 88) - 87 = 1pt
 * Paper	(Y, 89) - 87 = 2 pts
 * Scissor	(Z, 90) - 87 = 3 pts
 */
unsigned  solveDay2(char const *p) {
	unsigned score{0};

	char their_play{};
	char my_play{};
	std::ifstream i{p};

	while( i >> their_play >> my_play) {
		score +=
			/* outcome */ (((my_play - their_play - 23 + 4) % 3) * 3) +
			/* my play */ my_play - 87;
	}

	return score;
}


unsigned solveDay2b(char const *p) {
	unsigned score{0};

	char their_play{};
	char outcome{};
	std::ifstream i{p};

	while ( i >> their_play >> outcome) {
		score +=
		 /* outcome */ ((outcome - 1) % 3 * 3) +
		 /* my play */ ((their_play + outcome - 1) % 3 + 1);
	}

	return score;
}


int main(int, char **argv) {
	std::cout << "Pt1: " << solveDay2(argv[1]) << std::endl;
	std::cout << "Pt2: " << solveDay2b(argv[1]) << std::endl;
}
