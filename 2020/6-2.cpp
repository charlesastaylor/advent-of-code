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
    vector<char> group_used;
    int sum = 0;
    bool first = true;
    while (getline(file, str)) {
        if (str.empty()) {
            sum += group_used.size();
            group_used.clear();
            first = true;
            continue;
        }

        if (first) {
            for (char c: str) group_used.push_back(c);
            sort(group_used.begin(), group_used.end());
            first = false;
        } else {
            vector<char> person_used(str.begin(), str.end());
            vector<char> tmp;
            sort(person_used.begin(), person_used.end());
            set_intersection(group_used.begin(), group_used.end(),
                person_used.begin(), person_used.end(), back_inserter(tmp));
            group_used = tmp;
        }
    }

    int answer = sum + group_used.size(); // include the final group
    cout << "Answer: " << answer << endl;
    return 0;
}
