#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<ll, 2>;

ii ba, bb, prize;
string line;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  int state = 0;

  ll ans = 0;

  auto solve = [&]() -> void {
    int mn = INT_MAX;
    for (int i = 0; i <= 100; i++) {
      for (int j = 0; j <= 100; j++) {
        if (i*ba[0]+j*bb[0] == prize[0] && i*ba[1]+j*bb[1] == prize[1]) {
          mn = min(mn, 3*i + j);
        }
      }
    }
    if (mn != INT_MAX) {
      ans += mn;
    }
  };

  while (getline(cin, line)) {
    if (empty(line)) {
      solve();
      state = 0;
      continue;
    }
    if (state == 0) {
      auto parsed = line
        | views::split("+"sv)
        | ranges::to<vector<string>>();
      stringstream ss(parsed[1]);
      ss >> ba[0];
      stringstream __(parsed[2]);
      __ >> ba[1];
    } else if (state == 1) {
      auto parsed = line
        | views::split("+"sv)
        | ranges::to<vector<string>>();
      stringstream ss(parsed[1]);
      ss >> bb[0];
      stringstream __(parsed[2]);
      __ >> bb[1];
    } else {
      auto parsed = line
        | views::split("="sv)
        | ranges::to<vector<string>>();
      stringstream ss(parsed[1]);
      ss >> prize[0];
      stringstream __(parsed[2]);
      __ >> prize[1];
    }
    state++;
  }

  solve();

  cout << ans << '\n';

  return 0;
}
