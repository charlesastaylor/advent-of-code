#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;


int main(int argc, char *argv[]) {
    vector<u64> numbers = {1,12,0,20,8,16};

    for (int turn = numbers.size() + 1; turn <= 2020 ; turn++) {
        u64 last_number = numbers.back();
        u64 new_number = 0;
        for (int i = numbers.size() - 2; i >= 0; i--) {
            if (numbers[i] == last_number) {
                new_number = (turn - 2) - i;
                break;
            }
        }
        numbers.push_back(new_number);
    }

    cout << "Answer: " << numbers.back() << endl;

    return 0;
}