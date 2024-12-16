#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
int n;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  ll ans = 0;

  while (cin >> line) {
    n = ssize(line);

    vector<char> stk;
    string x, y;

    auto reset = [&]() -> void {
      stk.clear(), x.clear(), y.clear();
    };

    for (int i = 0; i < n; i++) {
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
    }
  }

  cout << ans << '\n';

  return 0;
}
