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

struct v2 {
    int x;
    int y;

    v2 operator+ (v2 const &obj) {
        v2 res;
        res.x = x + obj.x;
        res.y = y + obj.y;
        return res;
    }

    friend ostream& operator<<(ostream& os, const v2& v) {
        os << '(' << v.x << ',' << v.y << ')';
        return os;
    }
};

v2 rotate_by_90(v2& v, bool clockwise) {
    v2 res;
    res.x = clockwise ? v.y : -v.y;
    res.y = clockwise ? -v.x : v.x;
    return res;
}

void do_action(v2& ship, v2& waypoint, char action, int value) {
    if (action == 'F') {
        ship.x = ship.x + value * waypoint.x;
        ship.y = ship.y + value * waypoint.y;
    } else if (action == 'L') {
        int num_rotations = value / 90;
        while (num_rotations > 0) {
            waypoint = rotate_by_90(waypoint, false);
            num_rotations--;
        }
    } else if (action == 'R') {
        int num_rotations = value / 90;
        while (num_rotations > 0) {
            waypoint = rotate_by_90(waypoint, true);
            num_rotations--;
        }
    } else if (action == 'N') waypoint.y += value;
    else if (action == 'E') waypoint.x += value;
    else if (action == 'S') waypoint.y -= value;
    else if (action == 'W') waypoint.x -= value;
}

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    ifstream file("12a.txt");

    string str;
    int answer;
    v2 ship = {0, 0};
    v2 waypoint = {10, 1};
    while (getline(file, str)) {
        stringstream ss(str);
        char action;
        int value;
        ss >> action >> value;
        do_action(ship, waypoint, action, value);
        // cout << action << " - " << value << endl;
        // cout << "Ship: " << ship << ", Waypoint: " << waypoint << endl;
    }

    answer = abs(ship.x) + abs(ship.y);
    cout << "Answer: " << answer << endl;

    return -1;
}
