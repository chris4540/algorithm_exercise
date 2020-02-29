#include "vertex.hpp"
#include <iostream>
using namespace std;

template <typename V, typename E>
class Edge {
  private:
    const Vertex<V>& startVertex;
    const Vertex<V>& endVertex;
  public:
    Edge(Vertex<V>& start, Vertex<V>& end, E val):
        startVertex(start), endVertex(end), element(val) {
            cout << &startVertex << endl;
            cout << &endVertex << endl;
        };
    E element;
    E& operator*() {
        return element;
    }
    void endVertices() {};
    void opposite() {};
    void isAdjacentTo() {};
    void isIncidentOn(const Vertex<V>& v) {throw "this function is not implemented yet.";};
};
