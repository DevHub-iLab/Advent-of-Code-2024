#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<ll, 2>;

ii ba, bb, prize;
string line;

constexpr ll OFFSET = 10000000000000;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  int state = 0;

  ll ans = 0;

  auto solve = [&]() -> void {
    const ll DET = ba[0]*bb[1] - ba[1]*bb[0];

    ll take_a = bb[1]*prize[0] - bb[0]*prize[1];
    ll take_b = -ba[1]*prize[0] + ba[0]*prize[1];

    if (take_a%DET == 0 && take_b%DET == 0) {
      take_a /= DET, take_b /= DET;
      ans += 3LL*take_a + take_b;
    } else {
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
      prize[0] += OFFSET;
      prize[1] += OFFSET;
    }
    state++;
  }

  solve();

  cout << ans << '\n';

  return 0;
}
