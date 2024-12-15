#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

int n, m;
string raw;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  cin >> raw, n = ssize(raw);

  vector<ll> line;

  for (int i = 0; i < n; i++) {
    if (i%2 == 0) {
      for (int j = 0; j < raw[i]-'0'; j++) {
        line.push_back(i/2);
      }
    } else {
      for (int j = 0; j < raw[i]-'0'; j++) {
        line.push_back(-1);
      }
    }
  }

  m = ssize(line);

  for (int i = 0, j = m-1; i < j; i++) {
    while (j > i && line[j] == -1) j--;
    if (line[i] == -1) swap(line[i], line[j--]);
  }

  ll ans = 0;

  for (int i = 0; i < m; i++) {
    if (line[i] == -1) break;
    ans += line[i]*i;
  }

  cout << ans << '\n';

  return 0;
}
