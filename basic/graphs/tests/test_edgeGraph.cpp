#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "graph.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

TEST_CASE( "Extract Edges from graph", "[Edges]" ) {
    EdgeListGraph<string, string> g;
    g.insertEdge(string("vertex_called_u"), string("vertex_called_v"), string("edge_called_a"));

    auto edges = g.getEdges();
    auto edge = edges[0];
    auto vertices = edge->endVertices();

    // check the ans
    string vert1_name(**(vertices.first));
    string vert2_name(**(vertices.second));
    string edge_name(**edge);

    REQUIRE(vert1_name == string("vertex_called_u"));
    REQUIRE(vert2_name == string("vertex_called_v"));
    REQUIRE(edge_name == string("edge_called_a"));
}
