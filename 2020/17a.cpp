#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

struct v3 {
    int x = 0;
    int y = 0;
    int z = 0;

    v3 operator+ (v3 const &obj) {
        v3 res;
        res.x = x + obj.x;
        res.y = y + obj.y;
        res.z = z + obj.z;
        return res;
    }

    bool operator== (v3 const &w) {
        return x == w.x && y == w.y && z == w.z; 
    }

    friend ostream& operator<<(ostream& os, const v3& v) {
        os << "(" << v.x << ", " << v.y << ", " << v.z << ")";
        return os;
    }
};

vector<v3> get_neighbours(v3 v) {
    vector<v3> res = {
        {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1},
        {1, 1, 0}, {-1, -1, 0}, {1, -1, 0}, {-1, 1, 0},
        {1, 0, 1}, {1, 0, -1}, {-1, 0, 1}, {-1, 0, -1},
        {0, 1, 1}, {0, 1, -1}, {0, -1, 1}, {0, -1, -1},
        {1, 1, 1}, {-1, 1, 1}, {1, -1, 1}, {1, 1, -1},
        {-1, -1, 1}, {-1, 1, -1}, {1, -1, -1}, {-1, -1, -1},
    };
    for (int i = 0; i < res.size(); i++) res[i] = res[i] + v;
    return res;
}

vector<v3> active;
bool is_active(v3& v) {
    return find(active.begin(), active.end(), v) != active.end();
}

int main(int argc, char *argv[]) {
    ifstream file("17a.txt");
    // ifstream file("test.txt");
    string line;
    // set<v3> active;
    int line_number = 0;
    while (getline(file, line)) {
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '#') active.push_back({i, line_number, 0});
        }
        line_number++;
    }


    for (int cycle = 1; cycle <= 6; cycle++) {
        vector<v3> new_active;

        for (v3 a : active) {
            int neighbours_active = 0;
            vector<v3> neighbours = get_neighbours(a);
            for (v3 n : neighbours) {
                if (is_active(n)) neighbours_active++;

                int inner_neighbours_active = 0;
                for (v3 inner_n : get_neighbours(n)) {
                    if (is_active(inner_n)) inner_neighbours_active++;
                }

                if (is_active(n)) {
                    if (inner_neighbours_active == 2 || inner_neighbours_active == 3) {
                        if (find(new_active.begin(), new_active.end(), n) == new_active.end()) new_active.push_back(n);
                    }
                }
                else {
                    if (inner_neighbours_active == 3) {
                        if (find(new_active.begin(), new_active.end(), n) == new_active.end()) new_active.push_back(n);
                    }
                }
            }

            if (neighbours_active == 2 || neighbours_active == 3) {
                if (find(new_active.begin(), new_active.end(), a) == new_active.end()) new_active.push_back(a);
            }

        }
        active = new_active;
        cout << "active: " << active.size() << endl;
    }

    cout << "Answer: " << active.size() << endl;
    return 0;
}