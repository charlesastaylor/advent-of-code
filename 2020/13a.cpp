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

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    ifstream file("13a.txt");

    string str;
    int earliest_bus = 0;
    int minutes_to_wait = INT_MAX;
    getline(file, str);
    int earliest_depature = stoi(str);
    getline(file, str);
    // cout << earliest_depature << " - " << str << endl;
    stringstream ss(str);
    int bus_id;
    while (!ss.eof()) {
        if (isdigit((char)ss.peek())) {
            ss >> bus_id;
            // cout << "Found bus id: " << bus_id << endl;
            int tmp = bus_id * ((earliest_depature / bus_id) + 1) - earliest_depature;
            if (tmp < minutes_to_wait) {
                minutes_to_wait = tmp;
                earliest_bus = bus_id;
            }
        } else ss.get();
    }

    // cout << "Bus: " << earliest_bus << ", wait: " << minutes_to_wait << endl;
    cout << "Answer: " << earliest_bus * minutes_to_wait << endl;
    return -1;
}
