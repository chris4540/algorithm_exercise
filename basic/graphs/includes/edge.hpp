template <typename E>
class Edge {
public:
    E element;
    Edge(E val):
        element(val){};
    E& operator*() {
        return element;
    }
};
