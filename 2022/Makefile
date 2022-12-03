CXXFLAGS = -std=c++20 -pedantic -Wall -Wconversion -Werror -Wextra -Wpedantic -Wshadow

# Build the solution for the day by passing it as the target to make.
%.out: %.cpp
	${CXX} ${CXXFLAGS} $< -o $@
