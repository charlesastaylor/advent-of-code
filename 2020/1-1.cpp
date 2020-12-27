#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file("1-1.txt");
    string str;
    vector<int> ints;
    while (getline(file, str)) {
        ints.push_back(stoi(str));
    }
    for (int i = 0; i < ints.size(); i++) {
        for (int j = 0; j < ints.size(); j++) {
            if (i == j) continue;
            if (ints[i] + ints[j] == 2020) {
                cout << "a: " << ints[i] << ", b: " << ints[j] << ", prod: " << ints[i] * ints[j] << endl;
                return 0;
            }
        }
    }
    cout << "uh oh!" << endl;
    return 0;
}