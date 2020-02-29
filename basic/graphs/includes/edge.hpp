#ifndef EDGE_HPP
#define EDGE_HPP
#include "vertex.hpp"
#include <iostream>
#include <utility>

using namespace std;

template <typename V, typename E>
class Edge {
  private:
    Vertex<V>* startVertex;
    Vertex<V>* endVertex;
    E element;
  public:
    Edge(Vertex<V>& start,  Vertex<V>& end, const E& val):
        startVertex(&start), endVertex(&end), element(val){};
    E& operator*() {
      return element;
    }
    E operator*() const {
      return element;
    }
    pair<Vertex<V>*,  Vertex<V>*> endVertices() {
      return make_pair(startVertex, endVertex);
    };

    /**
     * Return the end vertex of edge e distinct from vertex v
     *
     * @param v: The pointer of the vertex v
     * @return Return the end vertex of this edge distinct from the input vertex v
     * @throws
     */
    Vertex<V>* opposite(Vertex<V>* v) {
      Vertex<V>* ret = nullptr;

      if (v == startVertex) ret = endVertex;
      if (v == endVertex) ret = startVertex;

      if (ret == nullptr) {
        throw invalid_argument(string("The input vertex is not incident to this edge"));
      }
      return ret;
    };
    void isAdjacentTo() {};
    void isIncidentOn(const Vertex<V>& v) {throw "this function is not implemented yet.";};
};
#endif
