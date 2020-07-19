//
// http://codeforces.com/problemset/problem/1380/B
// Solved by Louis + Paul, 2020-07-19
//

#include <iostream>
#include <string>
#include <algorithm>

std::string universalSolution(std::string bot) {
    int r = 0, p = 0, s = 0;
    for (char i : bot) {
        if (i == 'R') r++;
        if (i == 'P') p++;
        if (i == 'S') s++;
    }

    std::string outp;
    int m = std::max(r, std::max(p, s));
    if (r == m) outp += 'P';
    if (p == m) outp += 'S';
    if (s == m) outp += 'R';

    int diff = bot.length() - outp.length();
    for (int i = 0; i < diff; i++) {
        outp += outp[i % 3];
    }
    return outp;
}

int main() {
    int test_amount;
    std::cin >> test_amount;

    for (int i = 0; i < test_amount; i++) {
        std::string bot;
        std::cin >> bot;
        std::cout << universalSolution(bot) << std::endl;
    }
    return 0;
}
