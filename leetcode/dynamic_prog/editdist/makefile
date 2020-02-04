CXX=g++
CXXFLAGS= -Wall -Warray-bounds -fbounds-check
editdist: editdist.o
	g++ -o $@ $<

.cpp.o:
	$(CXX) $(CXXFLAGS) 	-c $<

.PHONY: clean
clean:
	@rm -f *.o *.exe
