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

struct Constraint {
    u64 bus_id;
    u64 separation;
};

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    ifstream file("13a.txt");

    string str;
    getline(file, str);
    getline(file, str);
    stringstream ss(str);
    vector<Constraint> constraints;
    u64 first_bus_id;
    u64 bus_id;
    u64 sep = 0;
    bool first = true;
    while (!ss.eof()) {
        if (isdigit((char)ss.peek())) {
            ss >> bus_id;
            if (first) {
                first_bus_id = bus_id;
                first = false;
            } 
            else {
                constraints.push_back({bus_id, sep});
            }
            sep++;
        } else {
            char c;
            ss >> c;
            if (c == 'x') sep++;
        }
    }
    // constraints.clear();
    // constraints.push_back({907, 17});
    cout << "First: " << first_bus_id << endl;
    for (Constraint c : constraints) {
        cout << c.bus_id << " = " << c.separation << endl;
    }
    /*
        Lol! To solve this properly you should probably have done some maths with
        the gcds and the lcms to work out the answer quickly.

        While thinking of how to do that I just found the multiples between 17 and
        907 (the biggest bus id) that are valid and was looping over them and it hit
        on the answer eventually :)
    */
    u64 mult = 906;
    u64 timestamp;
    while (1) {
        bool done = true;
        timestamp = mult * first_bus_id;
        // cout << "Current timestamp: " << timestamp << '\n';
        for (Constraint c : constraints) {
            if ((timestamp + c.separation) % c.bus_id != 0) {
                
                done = false; 
                break;
            }
        }
        if (done) {
            cout << mult << " - " << timestamp <<endl;
            break;
            static int tmp = 0;
            if (tmp++ > 10) break;
        }
        mult += 907;
    }
    cout << "Answer: " << timestamp << endl;
    return -1;
}
