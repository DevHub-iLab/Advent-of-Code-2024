#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
int n;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  ll ans = 0;
  bool progress = true;

  while (cin >> line) {
    n = ssize(line);

    vector<char> stk;
    string x, y;

    auto reset = [&]() -> void {
      stk.clear(), x.clear(), y.clear();
    };

    auto check_start = [&](int i) -> bool {
      if (i >= 3) {
        string _ = string(begin(line)+i-3, begin(line)+i+1);
        if (_ == "do()") return true;
      }
      return false;
    };

    auto check_stop = [&](int i) -> bool {
      if (i >= 6) {
        string _ = string(begin(line)+i-6, begin(line)+i+1);
        if (_ == "don't()") return true;
      }
      return false;
    };

    auto solve = [&](int i) -> void {
      if (empty(stk)) {
        if (line[i] == 'm') stk.push_back('m');
        else reset();
      } else if (ssize(stk) == 1) {
        if (line[i] == 'u') stk.push_back('u');
        else reset();
      } else if (ssize(stk) == 2) {
        if (line[i] == 'l') stk.push_back('l');
        else reset();
      } else if (ssize(stk) == 3) {
        if (line[i] == '(') stk.push_back('(');
        else reset();
      } else if (ssize(stk) == 4) {
        if (ssize(x) <= 2 && '0' <= line[i] && line[i] <= '9') x += line[i];
        else if (ssize(x) >= 1 && line[i] == ',') stk.push_back(',');
        else reset();
      } else if (ssize(stk) == 5) {
        if (ssize(y) <= 2 && '0' <= line[i] && line[i] <= '9') y += line[i];
        else if (ssize(y) >= 1 && line[i] == ')') {
          ans += stoll(x)*stoll(y);
          reset();
        } else {
          reset();
        }
      } else {
        reset();
      }
    };

    for (int i = 0; i < n; i++) {
      if (check_start(i)) progress = true;
      if (check_stop(i)) progress = false;
      if (progress) solve(i);
      else reset();
    }
  }

  cout << ans << '\n';

  return 0;
}
