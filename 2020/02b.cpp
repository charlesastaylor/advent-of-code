#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file("2-1.txt");
    string str;
    int valid = 0;
    while (getline(file, str)) {
        stringstream stream(str);
        int lower, upper;
        char c, _;
        string s;
        stream >> lower >> _ >> upper >> c >> _ >> s;
        lower--; upper--;
        if ((s[lower] == c || s[upper] == c) && !(s[lower] == c && s[upper] == c)) {
            valid++;
        } 
        // cout << lower << upper << c << s << endl;
    }
    
    cout << "Num valid: " << valid << endl;
    return 0;
}