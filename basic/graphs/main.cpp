#include "graph.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

    EdgeListGraph<string, string> g;
    g.insertEdge(string("u"), string("v"), string("a"));
    g.insertEdge(string("v"), string("w"), string("b"));
    g.insertEdge(string("u"), string("w"), string("c"));
    g.insertEdge(string("w"), string("z"), string("d"));

    g.print();

}
