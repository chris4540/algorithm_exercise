CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check -std=c++17
INCLUDE= -I./includes

main.x: main.o
	g++ $(CXXFLAGS) -o $@ $<

main.o: main.cpp ./includes/*.hpp
	$(CXX) $(CXXFLAGS) $(INCLUDE) -c $<

.PHONY: clean
clean:
	@rm -f *.o *.x
