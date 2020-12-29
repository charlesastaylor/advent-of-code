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

enum class Direction {
    North = 0,
    East = 1,
    South = 2,
    West = 3
};

struct Ship {
    int x = 0;
    int y = 0;
    Direction d = Direction::East;
    
    friend ostream& operator<<(ostream& os, const Ship& s) {
        char dir;
        switch (s.d) {
            case Direction::North: dir = 'N'; break;
            case Direction::East: dir = 'E'; break;
            case Direction::South: dir = 'S'; break;
            case Direction::West: dir = 'W'; break;
        }
        os << '(' << s.x << ',' << s.y << ',' << dir << ')';
        return os;
    }
};

void do_action(Ship& s, char action, int value) {
    if (action == 'F') {
        if (s.d == Direction::North) s.y += value;
        else if (s.d == Direction::South) s.y -= value;
        else if (s.d == Direction::East) s.x += value;
        else if (s.d == Direction::West) s.x -= value;
    } else if (action == 'L') {
        int new_dir = (int)s.d;
        new_dir = (new_dir - value / 90) % 4;
        if (new_dir < 0) new_dir += 4;  // % is not modulo!!!
        // cout << "new dir " << new_dir << endl;
        s.d = (Direction)new_dir;
    } else if (action == 'R') {
        int new_dir = (int)s.d;
        new_dir = (new_dir + value / 90) % 4; 
        if (new_dir < 0) new_dir += 4;  // % is not modulo!!!
        s.d = (Direction)new_dir;
    } else if (action == 'N') s.y += value;
    else if (action == 'E') s.x += value;
    else if (action == 'S') s.y -= value;
    else if (action == 'W') s.x -= value;
}

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    ifstream file("12a.txt");

    string str;
    int answer;
    Ship ship;
    while (getline(file, str)) {
        stringstream ss(str);
        char action;
        int value;
        ss >> action >> value;
        do_action(ship, action, value);
        // cout << action << " - " << value << endl;
        // cout << "Ship after action: "<< ship << endl;
        // if (action == 'L')
        //     cin.get();
    }

    answer = abs(ship.x) + abs(ship.y);
    cout << "Answer: " << answer << endl;

    return -1;
}
