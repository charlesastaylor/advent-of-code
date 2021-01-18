#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

struct v4 {
    int x = 0;
    int y = 0;
    int z = 0;
    int w = 0;

    v4 operator+ (v4 const &obj) {
        v4 res;
        res.x = x + obj.x;
        res.y = y + obj.y;
        res.z = z + obj.z;
        res.w = w + obj.w;
        return res;
    }

    friend bool operator==(const v4& lhs, const v4& rhs) {
        return lhs.x == rhs.x && lhs.y == rhs.y && lhs.z == rhs.z && lhs.w == rhs.w; ;
    }

    friend ostream& operator<<(ostream& os, const v4& v) {
        os << "(" << v.x << ", " << v.y << ", " << v.z << ", " << v.w << ")";
        return os;
    }

    struct HashFunction {
        size_t operator()(const v4& v) const {
            return hash<int>()(v.x) ^ hash<int>()(v.y) ^ hash<int>()(v.z) ^ hash<int>()(v.w);
        }
    };
};

typedef unordered_set<v4, v4::HashFunction> active_set; 

active_set get_neighbours(v4 v) {
    active_set out;
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            for (int k = -1; k <= 1; k++) {
                for (int l = -1; l <= 1; l++) {
                    v4 delta = {i, j, k, l};
                    out.insert(delta + v);
                }
            }
        }
    }
    out.erase(v);
    return out;
}

// bool is_active(v4& v) {
//     return find(active.begin(), active.end(), v) != active.end();
// }

int main(int argc, char *argv[]) {
    ifstream file("17a.txt");
    // ifstream file("test.txt");
    string line;
    active_set active;
    int line_number = 0;

    while (getline(file, line)) {
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '#') active.insert({i, line_number, 0, 0});
        }
        line_number++;
    }

    for (int cycle = 1; cycle <= 6; cycle++) {
        active_set new_active;

        for (v4 a : active) {
            int neighbours_active = 0;
            for (v4 n : get_neighbours(a)) {
                if (active.count(n)) neighbours_active++;

                int inner_neighbours_active = 0;
                for (v4 inner_n : get_neighbours(n)) {
                    if (active.count(inner_n)) inner_neighbours_active++;
                }

                if (active.count(n)) {
                    if (inner_neighbours_active == 2 || inner_neighbours_active == 3) new_active.insert(n);
                }
                else {
                    if (inner_neighbours_active == 3) new_active.insert(n);
                }
            }

            if (neighbours_active == 2 || neighbours_active == 3) new_active.insert(a);
        }
        active = new_active;
        cout << "active: " << active.size() << endl;
    }

    cout << "Answer: " << active.size() << endl;
    return 0;
}
