CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check

revint: revint.o
	g++ $(CXXFLAGS) -o $@ $<

.cpp.o:
	$(CXX) $(CXXFLAGS) -c $<

.PHONY: clean
clean:
	@rm -f *.o *.exe
