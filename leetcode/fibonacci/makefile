
solution.exe: solution.o
	g++ -o $@ $<

%.o : %.cpp
	g++ -c $<


.PHONY: clean
clean:
	rm *.o *.exe
