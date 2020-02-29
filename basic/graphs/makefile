CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check -std=c++2a
INCLUDE= -I./includes

main.x: main.o
	g++ $(CXXFLAGS) -o $@ $<

.cpp.o:
	$(CXX) $(CXXFLAGS) $(INCLUDE) -c $<

.PHONY: clean
clean:
	@rm -f *.o *.x
