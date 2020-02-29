SOURCES := $(wildcard test_*.cpp)
FILES := $(SOURCES:.cpp=.x)

# OPTS
CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check -std=c++17
CATCH_SINGLE_INCLUDE=/usr/local/include/catch2
INCLUDES=../includes

all: $(FILES)

test_%.x: test_%.o
	g++ $(CXXFLAGS) -o $@ $<

%.o: %.cpp
	g++ $(CXXFLAGS) -I$(CATCH_SINGLE_INCLUDE) -I$(INCLUDES) -c $< -o $@

.PHONY: clean
clean:
	@rm -f *.o *.x
