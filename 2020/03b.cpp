#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

int main(int argc, char *argv[]) {
    ifstream file("3-1.txt");
    string str;
    vector<string> lines;
    while (getline(file, str)) {
        lines.push_back(str);
    }

    vector<pair<int, int>> slopes;
    slopes.push_back({1, 1});
    slopes.push_back({3, 1});
    slopes.push_back({5, 1});
    slopes.push_back({7, 1});
    slopes.push_back({1, 2});
    u64 prod = 1;
    int x, y, num_trees;
    for (auto slope : slopes) {
        x = y = num_trees = 0;
        int width = lines[0].length();
        while (y < lines.size()) {
            if (y > 0) {
                if (lines[y][x] == '#') num_trees++;
            }
            x = (x + slope.first) % width;
            y = y + slope.second;
        }
        prod *= num_trees;
    }
    cout << "Answer: " << prod << endl;
    return 0;
}