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

        // Consider vertex
        Vertex<V>* vert_1;
        Vertex<V>* vert_2;
        auto it = vertexList.find(u);
        if (it == vertexList.end()){
          // vertex not exists in the vertexList
          vert_1 = new Vertex<V>(u);       // create a new obj in heap
          vertexList.insert({u, vert_1});  // save it
        } else {
          vert_1 = it->second;             // get the pointer
        }
        // to the same thing
        it = vertexList.find(v);
        if (it == vertexList.end()){
          vert_2 = new Vertex<V>(v);
          vertexList.insert({v, vert_2});
        } else {
          vert_2 = it->second;
        }

        // create the edge
        Edge<V, E>* edge = new Edge<V, E>(*vert_1, *vert_2, edge_val);
        // insert them to internal collections
        vertexList.insert({u, vert_1});

        edgeList.insert({edge_val, edge});
    };
  public:
    vector<Edge<V, E>*> edges(){
      // Notes: There is no array of reference. But array of pointers
      vector<Edge<V, E>*> ret;

      for (auto const& [key, val] : edgeList){
        ret.push_back(val);
      }
      return ret;
    };
    void print() {
      // print the edge list
      cout << "Edge List: " << endl;
      for (auto const& [key, val] : edgeList){
        auto vertices = val->endVertices();
        cout << "Edge " << key << ": ";
        cout << **vertices.first << " -- " << **vertices.second;
        cout << endl;
      }
    };

    Edge<V, E>* getEdgeBy(const E& key){
      Edge<V, E>* ret = nullptr;

      auto it = edgeList.find(key);
      if (it != edgeList.end()){
        ret = it->second;
      }
      return ret;
    };
    Vertex<V>* getVertexBy(const V& key){
      Vertex<V>* ret = nullptr;
      auto it = vertexList.find(key);
      if (it != vertexList.end()){
        ret = it->second;
      }
      return ret;
    };
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
