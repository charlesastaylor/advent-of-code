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
        int count_ = count(s.begin(), s.end(), c);
        if (count_ >= lower && count_ <= upper) valid++;
        // cout << lower << upper << c << s << endl;
    }
    
    cout << "Num valid: " << valid << endl;
    return 0;
}