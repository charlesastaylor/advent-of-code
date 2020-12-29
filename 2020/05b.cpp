#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

int get_row(string s) {
    int lower = 0;
    int upper = 127;
    for (char c: s) {
        int delta = (upper + 1 - lower) / 2;
        if (c == 'F') upper -= delta;
        else /* c == B */ lower += delta;
    }
    return lower;
}

int get_column(string s) {
    int lower = 0;
    int upper = 7;
    for (char c: s) {
        int delta = (upper + 1 - lower) / 2;
        if (c == 'L') upper -= delta;
        else /* c == R */ lower += delta;
    }
    return lower;
}

int main(int argc, char *argv[]) {
    ifstream file("5-1.txt");
    // ifstream file("test.txt");
    string str;
    vector<int> seat_ids;
    while (getline(file, str)) {
        int row, column, id;
        row = get_row(str.substr(0, 7));
        column = get_column(str.substr(7, str.length()));
        // cout << "row" << row << ", column" << column << endl;
        id = row * 8 + column;
        seat_ids.push_back(id);
        // static int tmp = 0;
        // if (tmp++ > 10) break;
    }
    sort(seat_ids.begin(), seat_ids.end());

    int current, answer;
    for (int i = 0; i < seat_ids.size(); i++) {
        if (i == 0) current = seat_ids[0];
        else {
            if (seat_ids[i] != current + 1) {
                answer = current + 1;
                break;
            }
            current++;
        }
    }

    cout << "Answer: " << answer << endl;
    return 0;
}