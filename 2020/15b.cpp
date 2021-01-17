#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;

typedef unsigned long long u64;
typedef signed long long s64;

int main(int argc, char *argv[]) {
    vector<u64> starting_numbers = {1,12,0,20,8,16};
    map<u64, u64> history;

    for (int i = 0; i < starting_numbers.size() - 1; i++) {
        history.insert({starting_numbers[i], i + 1});
    }
    u64 goal = 30000000;
    u64 turn = starting_numbers.size() + 1;
    u64 last_spoken = starting_numbers.back();
    while (1) {
        u64 tmp = last_spoken;
        if (history.count(last_spoken) == 1) {
            last_spoken = (turn - 1) - history[last_spoken];
        }
        else {
            last_spoken = 0;
        }

        history[tmp] = turn - 1;

        if (turn == goal) break;

        turn++;
    }    

    cout << "Answer: " << last_spoken << endl;

    return 0;
}