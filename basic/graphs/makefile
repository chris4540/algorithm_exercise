CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check
INCLUDE= -I./includes

main: main.o
	g++ $(CXXFLAGS) -o $@ $<

.cpp.o:
	$(CXX) $(CXXFLAGS) $(INCLUDE) -c $<

.PHONY: clean
clean:
	@rm -f *.o *.exe
