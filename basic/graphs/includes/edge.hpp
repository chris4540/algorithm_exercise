#ifndef EDGE_HPP
#define EDGE_HPP
#include "vertex.hpp"
#include <iostream>
#include <utility>

using namespace std;

template <typename V, typename E>
class Edge {
  private:
    const Vertex<V>* startVertex;
    const Vertex<V>* endVertex;
    E element;
  public:
    Edge(Vertex<V>& start,  Vertex<V>& end, E& val):
        startVertex(&start), endVertex(&end), element(val){};
    E& operator*() {
      return element;
    }
    E operator*() const {
      return element;
    }
    pair<const Vertex<V>*, const Vertex<V>*> endVertices() const {
      return make_pair(startVertex, endVertex);
    };
    void opposite() {};
    void isAdjacentTo() {};
    void isIncidentOn(const Vertex<V>& v) {throw "this function is not implemented yet.";};
};
#endif
