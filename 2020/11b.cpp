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

char FLOOR = '.';
char EMPTY = 'L';
char FULL  = '#';

typedef vector<vector<char>> Grid;
typedef vector<char> Row;

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

void print_grid(Grid& grid) {
    for (Row row : grid) {
        for (char cell : row) {
            cout << cell;
        }
        cout << '\n';
    }
    cout << endl;
}

int num_adjacent_full(v2 cell, Grid& grid) {
    int width = grid[0].size();
    int height = grid.size();
    int num = 0;
    vector<v2> deltas = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    for (v2 delta : deltas) {
        v2 test = cell;
        // find first seat in this direction
        do {
            test = test + delta;
        } while (test.x >= 0 && test.x < width && test.y >= 0 && test.y < height && grid[test.y][test.x] == FLOOR);
        if (test.x < 0 || test.x >= width || test.y < 0 || test.y >= height) continue;
        if (grid[test.y][test.x] == FULL) num++;
    }
    return num;
}

char update_cell(v2 cell, Grid& grid) {
    if (grid[cell.y][cell.x] == EMPTY && num_adjacent_full(cell, grid) == 0) 
        return FULL;
    if (grid[cell.y][cell.x] == FULL && num_adjacent_full(cell, grid) >= 5)
        return EMPTY;
    return grid[cell.y][cell.x];
}

int main(int argc, char *argv[]) {
    // ifstream file("test.txt");
    ifstream file("11a.txt");

    string str;
    Grid grid;
    while (getline(file, str)) {
        vector<char> new_row;
        for (char c : str) {
            new_row.push_back(c);
        }
        grid.push_back(new_row);
    }
    int width = grid[0].size();
    int height = grid.size();

    Grid tmp_grid = grid;
    while (1) {
        // print_grid(grid);
        for (int j = 0; j < height; j++) {
            for (int i = 0; i < width; i++) {
                tmp_grid[j][i] = update_cell({i, j}, grid);
            }
        }
        if (grid == tmp_grid) break;
        grid = tmp_grid;
    }
    // print_grid(grid);

    int answer = 0;
    for (Row row : grid) {
        for (char cell : row) {
            if (cell == FULL) answer++;
        }
    }
    cout << "Answer: " << answer << endl;

    return -1;
}
