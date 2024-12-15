#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = pair<int, int>;

int n, m;
string raw;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  cin >> raw, n = ssize(raw);

  vector<ll> line;
  vector<ii> idxs;

  for (int i = 0; i < n; i++) {
    if (i%2 == 0) {
      idxs.push_back(ii{ ssize(line), (int)(raw[i]-'0') });
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

  auto check = [&](int i) -> int {
    int len = 0;
    while (i < m && line[i] == -1) len++, i++;
    return len;
  };

  for (int i = ssize(idxs)-1, j; i >= 0; i--) {
    auto [idx, req] = idxs[i];
    j = 0;
    while (j < idx && check(j) < req) j++;
    if (j < idx && check(j) >= req) {
      for (int k = 0; k < req; k++) {
        swap(line[idx+k], line[j+k]);
      }
    }
  }

  ll ans = 0;

  for (int i = 0; i < m; i++) {
    if (line[i] == -1) continue;
    ans += line[i]*i;
  }

  cout << ans << '\n';

  return 0;
}
