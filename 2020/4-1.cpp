#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

bool is_required_field(string s) {
    string required[7] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
    for (string r : required) {
        if (r == s) return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
    ifstream file("4-1.txt");
    string str;
    int fields_found = 0;
    int num_valid = 0;
    while (getline(file, str)) {
        if (str.empty()) {
            cout << fields_found << endl;
            if (fields_found >= 7) num_valid++;
            fields_found = 0;
            continue;
        }

        stringstream stream(str);
        string field;
        while (stream >> field) {
            string key = field.substr(0, 3);
            if (is_required_field(key)) fields_found++;
        }
    }
    if (fields_found >= 7) num_valid++;

    cout << "Answer: " << num_valid << endl;
    return 0;
}