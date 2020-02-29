#include "graph.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

    EdgeListGraph<string, string> g;
    g.insertEdge(string("u"), string("v"), string("a"));

    auto edges = g.getEdges();

    auto x = edges[0];
    auto vertices = x->endVertices();
    cout << "Edge: " << **x;
    cout << " => Vertex 1 : " << **(vertices.first);
    cout << " => Vertex 2 : " << **(vertices.second);
}
