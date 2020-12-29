#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file("3-1.txt");
    string str;
    vector<string> lines;
    while (getline(file, str)) {
        lines.push_back(str);
    }

    int x, y, num_trees;
    int width = lines[0].length();
    while (y < lines.size()) {
        if (y > 0) {
            if (lines[y][x] == '#') num_trees++;
        }
        x = (x + 3) % width;
        y = y + 1;
    }
    
    cout << "Num trees: " << num_trees << endl;
    return 0;
}