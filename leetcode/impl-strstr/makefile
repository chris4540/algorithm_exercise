CXX=g++

strstr: strstr.o
	g++ -o $@ $<

.cpp.o:
	$(CXX) -c $<

.PHONY: clean
clean:
	@rm -f *.o *.exe
