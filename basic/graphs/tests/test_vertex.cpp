#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <string>
#include "vertex.hpp"

using namespace std;

TEST_CASE( "Vertex Class dereference operator", "[vertex]" ) {
   string s = "chris";
   Vertex<string> v = Vertex<string>(s);

   REQUIRE((*v) == s);
}
