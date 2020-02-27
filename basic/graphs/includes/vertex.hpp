#include "element.hpp"

class Vertex {
public:
    Element* e_ptr;
    Vertex(Element* e) {
        e_ptr = e;
    };
    void incidentEdges() {};
    bool isAdjacentTo(const Vertex& s) {
        return false;
    };

    Element& operator*() {
        return *e_ptr;
    }
};
