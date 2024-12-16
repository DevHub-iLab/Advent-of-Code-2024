#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

int x, y, n;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<int> a, b;

  while (cin >> x >> y) {
    a.push_back(x), b.push_back(y);
    n++;
  }

  ranges::sort(a);
  ranges::sort(b);

  ll ans = 0;

  for (int i = 0; i < n; i++) {
    ans += abs(a[i]-b[i]);
  }

  cout << ans << '\n';

  return 0;
}
