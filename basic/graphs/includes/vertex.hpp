#ifndef VERTEX_HPP
#define VERTEX_HPP

template <typename V>
class Vertex {
public:
    V element;
    Vertex(V val):
        element(val){};
    void incidentEdges() {};
    bool isAdjacentTo(const Vertex& s) { return false;};

    V& operator*() {
        return element;
    }

    // make a constance method (no modufication to members) and return a copy of element
    V operator*() const {
        return element;
    }
};
#endif
