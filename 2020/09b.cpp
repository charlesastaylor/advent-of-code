#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <climits>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

bool is_sum(int a, vector<int>& preamble) {
    for (int x : preamble) {
        for (int y : preamble) {
            if (x == y) continue;
            if (x + y == a) return true;
        }
    }
    return false;
}

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    // u64 target = 127;
    ifstream file("9-1.txt");
    u64 target = 393911906;
    string str;

    vector<u64> numbers;
    while (getline(file, str)) {
        u64 current = stoull(str);
        numbers.push_back(current);
    }

    int lower = 0;
    int upper = 1;
    u64 sum;
    while (1) {
        sum = 0;
        for (int i = lower; i < upper; i++) {
            sum += numbers[i];
        }
        if (sum == target) break;
        else if (sum < target) upper++;
        else if (sum > target) lower++;
    }

    u64 min_ = ULLONG_MAX;
    u64 max_ = 0;
    for (int i = lower; i < upper; i++) {
        min_ = min(min_, numbers[i]);
        max_ = max(max_, numbers[i]);
    }
    cout << "Answer: " << min_ + max_ << endl;

    return -1;
}
