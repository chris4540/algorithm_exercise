# Graphs and related algorithms

## Programming language  
c++ 

## Reference book
Data Structures & Algorithms in C++ Goodrich

## List of algorithm
1. Impl. of graph
2. DFS
3. BFS
4. Dijkstra’s Algorithm
5. A* Search (https://courses.cs.washington.edu/courses/cse373/19au/homework/astar)

### Extra info
https://courses.cs.washington.edu/courses/cse373/19au/


### Java Impl.
https://github.com/fletchto99/CSI2110/tree/master/Labs/resources/net/datastructures

### References
https://github.com/mjwestcott/Goodrich

https://www.techiedelight.com/graph-implementation-using-stl/

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

https://courses.cs.washington.edu/courses/cse373/19wi/

https://github.com/carterene/data-and-algo

https://github.com/Lukas713/dataStructuresAndAlgorithms/blob/master/OOP/Graph/dijkstraAlgorithm.cpp

# Testing
We use catch2 as it is a simple framework [link](https://github.com/catchorg/Catch2)

```bash
$ git clone https://github.com/catchorg/Catch2.git
$ cd Catch2
$ cmake -Bbuild -H. -DBUILD_TESTING=OFF
$ sudo cmake --build build/ --target install
```
