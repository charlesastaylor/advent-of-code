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
            for (int k = 0; k < ints.size(); k++) {
                if (i == j || i == k || j == k) continue;
                if (ints[i] + ints[j] + ints[k] == 2020) {
                    cout << "a: " << ints[i] << ", b: " << ints[j] << ", c: " << ints[k] <<
                        ", prod: " << ints[i] * ints[j] * ints[k] << endl;
                    return 0;
                }
            }
        }
    }
    cout << "uh oh!" << endl;
    return 0;
}