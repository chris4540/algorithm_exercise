SOURCES := $(wildcard test_*.cpp)
FILES := $(SOURCES:.cpp=.x)

# OPTS
CATCH_SINGLE_INCLUDE=/usr/local/include/catch2
INCLUDES=../includes

all: $(FILES)

test_%.x: test_%.o
	g++ -o $@ $<

%.o: %.cpp
	g++ -std=c++11 -Wall -I$(CATCH_SINGLE_INCLUDE) -I$(INCLUDES) -c $< -o $@

.PHONY: clean
clean:
	@rm -f *.o *.x
