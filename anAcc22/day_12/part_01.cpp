#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

constexpr int DI = 4;

array<int, DI> di{ 0, 1, 0, -1 };
array<int, DI> dj{ 1, 0, -1, 0 };

int n, m;
string line;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) g.push_back(line), m = ssize(line);
  n = ssize(g);

  auto in_bound = [&](int i, int j) -> bool {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  vector seen(n, vector(m, false));

  ll ans = 0, area, peri;

  auto solve = [&](this auto self, int i, int j) -> void {
    area++;
    char c = g[i][j];
    seen[i][j] = true;
    for (int dd = 0; dd < DI; dd++) {
      int ni = i+di[dd], nj = j+dj[dd];
      if (!in_bound(ni, nj) || g[ni][nj] != c) { peri++; continue; }
      if (seen[ni][nj]) continue;
      self(ni, nj);
    }
  };

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (seen[i][j]) continue;
      area = peri = 0;
      solve(i, j);
      ans += area*peri;
    }
  }

  cout << ans << '\n';

  return 0;
}
