#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;


int main(int argc, char *argv[]) {
    ifstream file("6-1.txt");
    // ifstream file("test.txt");
    string str;
    set<char> used;
    int sum = 0;
    while (getline(file, str)) {
        if (str.empty()) {
            sum += used.size();
            used.clear();
            continue;
        }

        for (char c: str) used.insert(c);
    }

    int answer = sum + used.size(); // include the final group
    cout << "Answer: " << answer << endl;
    return 0;
}
