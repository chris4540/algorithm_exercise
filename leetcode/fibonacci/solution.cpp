/*

Naive way to have the fibonacci number

Reference:
https://leetcode.com/problems/fibonacci-number/

 */

#include<iostream>

using namespace std;

class Solution {
public:

    // Recursion version
    long fib_r(int N) {
        if (N <= 1) return N;
        return fib_r(N-1) + fib_r(N-2);
    }

    // simple version with mem
    long fib_mem(int N){
        if (N <= 1) return N;

        // make a cache
        long* cache = new long[N+1];

        cache[0] = 0;
        cache[1] = 1;

        for (int i = 2; i<=N; i++){
            cache[i] = cache[i-1] + cache[i-2];
        }

        long ret = cache[N];
        // deallocate
        delete [] cache;

        return ret;
    }

    long fib_simple(int N){
        if (N <= 1) return N;
        long prev = 1;
        long cur = 1;
        long next = -100;

        for (int i = 2; i<=N; i++){
            // calculate the next one
            next = prev + cur;

            // store the current solution as prev
            prev = cur;
            // move next to be current
            cur = next;
        }

        return cur;
    }

    // long fib(int N){ return fib_mem(N); }

};

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        int N = stringToInteger(line);

        // long ret = Solution().fib(N);

        // string out = to_string(ret);
        // cout << "Solution.fib: " << Solution().fib(N) << endl;
        // cout << "Solution.fib_mem: " << Solution().fib(N) << endl;
        cout << "Solution.fib_simple: " << Solution().fib_simple(N) << endl;
    }
    return 0;
}
