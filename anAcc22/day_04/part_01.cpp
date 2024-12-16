#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

constexpr int DI = 8, WORD = 4;

array<int, DI> di{ 0, 1, 1, 1, 0, -1, -1, -1 };
array<int, DI> dj{ 1, 1, 0, -1, -1, -1, 0, 1 };

string line;
int n, m ;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) {
    g.push_back(line);
    m = ssize(line);
  }

  n = ssize(g);

  auto in_bound = [&](int i, int j) -> bool {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  auto check = [&](int i, int j) -> int {
    int ans = 0;
    for (int d = 0; d < DI; d++) {
      int ni = i + di[d]*(WORD-1);
      int nj = j + dj[d]*(WORD-1);
      if (!in_bound(ni, nj)) continue;
      string cur = string(1, g[i][j]);
      for (int k = 1; k <= WORD-1; k++) {
        ni = i+di[d]*k, nj = j+dj[d]*k;
        cur += g[ni][nj];
      }
      if (cur == "XMAS") ans++;
    }
    return ans;
  };

  int ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      ans += check(i, j);
    }
  }

  cout << ans << '\n';

  return 0;
}
