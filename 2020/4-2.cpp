#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

bool is_required_field(string s) {
    string required[7] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
    for (string r : required) {
        if (r == s) return true;
    }
    return false;
}

bool is_valid_byr(string s) {
    if (s.length() != 4) return false;
    int byr = stoi(s);
    return byr >= 1920 && byr <= 2002;
}

bool is_valid_iyr(string s) {
    if (s.length() != 4) return false;
    int iyr = stoi(s);
    return iyr >= 2010 && iyr <= 2020;
}

bool is_valid_eyr(string s) {
    if (s.length() != 4) return false;
    int eyr = stoi(s);
    return eyr >= 2020 && eyr <= 2030;
}

bool is_valid_hgt(string s) {
    if (s.length() < 4) return false;
    string unit = s.substr(s.length() - 2, s.length());
    int height;
    if (unit == "cm") {
        height = stoi(s.substr(0, s.length() - 2));
        return height >= 150 && height <= 193;
    } else if (unit == "in") {
        height = stoi(s.substr(0, s.length() - 2));
        return height >= 59 && height <= 76;
    }
    return false;
}

bool is_valid_hcl(string s) {
    if (s.length() != 7) return false;
    if (s[0] != '#') return false;
    for (int i = 1; i <= 6; i++) {
        bool valid = false;
        for (char c : "0123456789abcdef") {
            if (s[i] == c) {
                valid = true;
                break;
            };
        }
        if (!valid) return false;
    }
    return true;
}

bool is_valid_ecl(string s) {
    for (string r : {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) {
        if (s == r) return true;
    }
    return false;
}

bool is_valid_pid(string s) {
    if (s.length() != 9) return false;
    for (char c : s) {
        if (!isdigit(c)) return false;
    }
    return true;
}

bool is_valid_field(string key, string value) {
    if (key == "byr") return is_valid_byr(value);
    else if (key == "iyr") return is_valid_iyr(value);
    else if (key == "eyr") return is_valid_eyr(value);
    else if (key == "hgt") return is_valid_hgt(value);
    else if (key == "hcl") return is_valid_hcl(value);
    else if (key == "ecl") return is_valid_ecl(value);
    else if (key == "pid") return is_valid_pid(value);
    else if (key == "cid") return false;
    else {
        cout << "uh ohhhhh!!!" << endl;
        return false;
    }
}

int main(int argc, char *argv[]) {
    // test functions
    // for (string s: {"2002", "2003"}) {
    //     cout << s << ": " << is_valid_byr(s) << endl;
    // }
    
    // for (string s: {"60in", "190cm", "190in", "190"}) {
    //     cout << s << ": " << is_valid_hgt(s) << endl;
    // }

    // for (string s: {"#123abc", "#123abz", "123abc"}) {
    //     cout << s << ": " << is_valid_hcl(s) << endl;
    // }

    // for (string s: {"brn", "wat"}) {
    //     cout << s << ": " << is_valid_ecl(s) << endl;
    // }

    // for (string s: {"000000001", "0123456789"}) {
    //     cout << s << ": " << is_valid_pid(s) << endl;
    // }

    ifstream file("4-1.txt");
    string str;

    int fields_found = 0;
    int num_valid = 0;
    while (getline(file, str)) {
        if (str.empty()) {
            if (fields_found >= 7) num_valid++;
            fields_found = 0;
            continue;
        }

        stringstream stream(str);
        string field;
        while (stream >> field) {
            string key = field.substr(0, 3);
            string value = field.substr(4, field.length());
            // cout << key << ": " << value << endl;
            if (is_valid_field(key, value)) fields_found++;
        }
    }
    if (fields_found >= 7) num_valid++;
    cout << "Answer: " << num_valid << endl;
    return 0;
}