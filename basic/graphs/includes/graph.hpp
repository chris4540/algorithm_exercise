#include <iostream>
#include "edge.hpp"
#include "vertex.hpp"

using namespace std;
template <typename V, typename E>
class Graph {
  public:
    Graph() { cout << "Calling Graph Constr." << endl;};
    void virtual print() = 0;
    void virtual insertEdge(
        const Vertex<V> &u, const Vertex<V> &v, const E &element) = 0;
};

template <typename V, typename E>
class EdgeListGraph : public Graph<V, E> {
  public:
    EdgeListGraph() { cout << "Calling EdgeListGraph Constr." << endl;}
    void insertEdge(const Vertex<V> &u, const Vertex<V> &v, const E &element) {
        cout << "Helloworld" << endl;
    };
    void print() {
        cout << "Helloworld" << endl;
    };
};
