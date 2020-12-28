#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

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
    // int preamble_length = 5;
    ifstream file("9-1.txt");
    int preamble_length = 25;
    string str;
    vector<int> preamble;
    while (getline(file, str)) {
        int current = stoi(str);
        if (preamble.size() < preamble_length) preamble.push_back(current);
        else {
            if (is_sum(current, preamble)) {
                preamble.push_back(current);
                preamble.erase(preamble.begin());
            } else {
                cout << "Answer: " << current << endl;
                return 0;
            }
        }
    }

    return -1;
}
