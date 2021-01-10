#include <iostream>
#include <string>
#include <math.h>
using namespace std;

bool is_prime(long n) {
    if (n < 2) return false;

    long upper_bound = sqrt(n);
    for (long num=2; num <= upper_bound; num++){
        if (n%num == 0) return false;
    }
    return true;
}

bool is_all_digit_prime(long n){
    long digit;
    while (n > 0){
        digit = n % 10l;
        if (!is_prime(digit)) return false;
        n = n / 10l;
    }
    return true;

}

int main(int argc, char *argv[]) {
    int d = atoi(argv[1]);
    int n = atoi(argv[2]);

    int out_cnt = 0;

    long start = pow(10, d-1);
    long end = pow(10, d) - 1;
    for (long num = start; num <= end; ++num){
        if (is_all_digit_prime(num) && is_prime(num)){
            cout << num << endl;
            ++out_cnt;
        }
        if (out_cnt >= n) {
            break;
        }
    }
    return 0;
}
