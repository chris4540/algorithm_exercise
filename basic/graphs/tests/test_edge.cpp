#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <string>
#include "vertex.hpp"
#include "edge.hpp"

using namespace std;

TEST_CASE( "Test Edge::opposite", "[edge]" ) {
    // char c = 'u';
    Vertex<char>* vert_1 = new Vertex<char>(char('u'));
    Vertex<char>* vert_2 = new Vertex<char>(char('v'));
    Edge<char, char>* edge = new Edge<char, char>(*vert_1, *vert_2, ' ');

    auto u = edge->opposite(vert_2);
    REQUIRE(**u == 'u');
    auto v = edge->opposite(vert_1);
    REQUIRE(**v == 'v');
}
