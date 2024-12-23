#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
ll test_value = 0;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  ll ans = 0;

  while (getline(cin, line)) {
    auto parsed = line
      | views::split(" "sv)
      | ranges::to<vector<string>>();
    stringstream test_value_ss(parsed[0]);

    test_value_ss >> test_value;

    vector<int> a;
    for (int i = 1; i < ssize(parsed); i++) a.push_back(stoll(parsed[i]));

    int n = ssize(a);
    bool ok = false;

    auto solve = [&](auto &&self, ll cur, int idx) -> void {
      if (cur > test_value) return;
      if (idx == n) {
        ok |= (cur == test_value);
        return;
      }
      self(self, cur*a[idx], idx+1);
      self(self, cur+a[idx], idx+1);
    };

    solve(solve, a[0], 1);

    if (ok) ans += test_value;
  }

  cout << ans << '\n';

  return 0;
}