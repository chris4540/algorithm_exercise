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
};
