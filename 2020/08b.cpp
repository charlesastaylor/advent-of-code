#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

bool have_already_visited(vector<int>& visited, int i) {
    for(int v : visited) {
        if (v == i) return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
    ifstream file("8-1.txt");
    // ifstream file("test.txt");
    string str;
    vector<pair<string, int>> original_program;
    while (getline(file, str)) {
        stringstream stream(str);
        string op; int arg;
        stream >> op >> arg;
        original_program.push_back({op, arg});
    }

    int head, acc;
    vector<int> visited;
    vector<pair<string, int>> program;

    for (auto& instruction : original_program) {
        if (instruction.first == "acc") continue;

        if (instruction.first == "nop") instruction.first = "jmp";
        else instruction.first = "nop";
        program = original_program; // hope this copies!
        visited.clear();
        head = acc = 0;
        if (instruction.first == "nop") instruction.first = "jmp";
        else instruction.first = "nop";

        do {
            visited.push_back(head);
            string op = program[head].first;
            if (op == "acc") {
                acc += program[head].second;
                head++;
            } else if (op == "jmp") {
                head += program[head].second;
            } else if (op == "nop") {
                head++;
            } else cout << "Panic!" << endl;

            if (head >= program.size()) {
                cout << "Success! Answer: " << acc << endl;
                return 0;
            }
        } while (!have_already_visited(visited, head));
    }

    cout << "Answer: " << acc << endl;
    return 0;
}
