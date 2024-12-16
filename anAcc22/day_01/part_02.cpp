#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

int x, y, n;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<int> a, b;
  map<int, int> bcnt;

  while (cin >> x >> y) {
    a.push_back(x), b.push_back(y);
    bcnt[y]++;
    n++;
  }

  ll ans = 0;

  for (auto &i : a) {
    ans += (ll)i*bcnt[i];
  }

  cout << ans << '\n';

  return 0;
}
