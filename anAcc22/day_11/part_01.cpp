#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  getline(cin, line);
  auto parsed = line
    | views::split(" "sv)
    | ranges::to<vector<string>>();

  map<string, ll> mp;

  for (auto &s : parsed) mp[s]++;

  for (int i = 1, n; i <= 25; i++) {
    map<string, ll> new_mp;
    for (auto &[s, cnt] : mp) {
      if (s == "0") new_mp["1"] += cnt;
      else if (ssize(s)%2 == 0) {
        n = ssize(s);
        auto f = string(begin(s), begin(s)+n/2);
        auto b = string(begin(s)+n/2, end(s));
        ranges::reverse(b);
        while (ssize(b) >= 2 && b.back() == '0') b.pop_back();
        ranges::reverse(b);
        new_mp[f] += cnt;
        new_mp[b] += cnt;
      } else {
        new_mp[to_string(stoll(s)*2024LL)] += cnt;
      }
    }
    mp = new_mp;
  }

  ll ans = 0;

  for (auto &[_, cnt] : mp) ans += cnt;

  cout << ans << '\n';

  return 0;
}
