#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <memory>
#include "edge.hpp"
#include "vertex.hpp"

using namespace std;
template <typename V, typename E>
class AbstractGraph {
  public:
    // Graph() { cout << "Calling Graph Constr." << endl;};
    void virtual print() = 0;
    virtual ~AbstractGraph() = default;
    // void virtual insertEdge(Vertex<V> &u, Vertex<V> &v, E &element) = 0;
};

template <typename V, typename E>
class EdgeListGraph : public AbstractGraph<V, E> {
  private:
    // implement the vertex edge collection using map
    map<E, Edge<V, E>*> edgeList;
    map<V, Vertex<V>*> vertexList;
  public:
    EdgeListGraph() {};
    ~EdgeListGraph() {
      // delete vertex
      for (auto const& [key, val] : vertexList){
        delete val;
      }
      // delete edge
      for (auto const& [key, val] : edgeList){
        delete val;
      }
    }
    void insertEdge(V u, V v, E edge_val) {
        // Vertex<V>* vert_1 = new Vertex<V>(u);
        Vertex<V>* vert_1(new Vertex<V>(u));
        Vertex<V>* vert_2(new Vertex<V>(v));

        Edge<V, E>* edge = new Edge<V, E>(*vert_1, *vert_2, edge_val);

        // insert them to internal collections
        vertexList.insert({u, vert_1});
        vertexList.insert({v, vert_2});
        edgeList.insert({edge_val, edge});
    };
  public:
    vector<Edge<V, E>*> getEdges(){
      // Notes: There is no array of reference. But array of pointers
      vector<Edge<V, E>*> ret;

      for (auto const& [key, val] : edgeList){
        ret.push_back(val);
      }
      return ret;
    };
    void print() {};
};

// Graph Implementation using adjacency list
template <typename V, typename E>
class AdjacencyListGraph : public AbstractGraph<V, E> {
    // TODO
};

template <typename V, typename E>
class AdjacencyMapGraph : public AbstractGraph<V, E> {
    // TODO
};
