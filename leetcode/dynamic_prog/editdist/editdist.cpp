#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        string s = "-" + word1;
        string t = "-" + word2;
        int m = s.size();
        int n = t.size();

        // iterators
        int i, j;

        // make a distance matrix to store the min-edit distance of partial words
        int dists[m][n] = {0};

        // the edge results are simple, calculate them first
        // equiv. to remove/insert all letters
        for (i = 1; i < m; i++) dists[i][0] = i;
        for (j = 1; j < n; j++) dists[0][j] = j;

        // move (i, j) to (m, n) until we get the min dist
        for (i = 1; i < m; i++){
            for (j = 1; j < n; j++) {

                // the cost of subsitution a char
                // if (i, j) char are the same, cost = 0 else 1;
                int cost = (s[i] == t[j]) ? 0 : 1;

                // the update val
                int val = min(
                    dists[i-1][j-1] + cost, // sub cost
                    min(
                    dists[i-1][j] + 1, // delete cost
                    dists[i][j-1] + 1  // insert cost
                ));

                dists[i][j] = val;
            }
        }

        return dists[m-1][n-1];
    }
};


string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

int main() {
    string line;
    while (getline(cin, line)) {
        string word1 = stringToString(line);
        getline(cin, line);
        string word2 = stringToString(line);

        int ret = Solution().minDistance(word1, word2);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
