#include <iostream>
#include <stdio.h>
#include <map>
#include "edge.hpp"
#include "vertex.hpp"

using namespace std;
template <typename V, typename E>
class Graph {
  public:
    // Graph() { cout << "Calling Graph Constr." << endl;};
    void virtual print() = 0;
    // void virtual insertEdge(Vertex<V> &u, Vertex<V> &v, E &element) = 0;
};

template <typename V, typename E>
class EdgeListGraph : public Graph<V, E> {
  private:
    // implement the vertex edge collection using map
    map<E, Edge<V, E>&> edgeList;
    map<V, Vertex<V>&> vertexList;
  public:
    EdgeListGraph() { cout << "Calling EdgeListGraph Constr." << endl;};
    void insertEdge(V u, V v, E edge_val) {
        Vertex<V> vert_1(u);
        Vertex<V> vert_2(v);
        Edge<V, E> edge(vert_1, vert_2, edge_val);

        vertexList.insert({u, vert_1});
        vertexList.insert({v, vert_1});


    };
    void print() {
        cout << "Helloworld" << endl;
    };
};

// Graph Implementation using adjacency list
template <typename V, typename E>
class AdjacencyListGraph : public Graph<V, E> {
    // TODO
};

template <typename V, typename E>
class AdjacencyMapGraph : public Graph<V, E> {
    // TODO
};
