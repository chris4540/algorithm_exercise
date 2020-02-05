#include <string>
#include <iostream>
#include <cassert>
#include <limits>
using namespace std;

// ---------------------------------------------------
class Solution {
public:
    int reverse(int x) {
        int ret = 0;

        while (x != 0) {
            // shift 1 pos in decimal system
            if (mulOverflow(ret, 10)) {
                return 0;
            } else {
                ret = ret * 10;
            }

            ret += (x % 10);
            // div by 10
            x /= 10;
        }

        return ret;
    }
private:

    // check if (a * b) sum to a overflow number
    bool mulOverflow(int a, int b){
        assert(b > 0);
        if (a > numeric_limits<int>::max() / b ||
            a < numeric_limits<int>::min() / b) {
            return true;
        } else{
            return false;
        }

    }
};
// ---------------------------------------------------
int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        int x = stringToInteger(line);

        int ret = Solution().reverse(x);

        string out = to_string(ret);
        cout << "------------------" << endl;
        cout << "Input = " << x << endl;
        cout << "Output = " << out << endl;
    }
    return 0;
}
