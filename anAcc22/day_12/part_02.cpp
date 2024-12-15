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

  map<int, vector<int>> top_mp_ij;
  map<int, vector<int>> bot_mp_ij;

  map<int, vector<int>> left_mp_ji;
  map<int, vector<int>> right_mp_ji;

  ll ans = 0, area, peri;

  auto solve = [&](this auto self, int i, int j) -> void {
    area++;
    char c = g[i][j];
    seen[i][j] = true;
    for (int dd = 0; dd < DI; dd++) {
      int ni = i+di[dd], nj = j+dj[dd];
      if (!in_bound(ni, nj) || g[ni][nj] != c) {
        if (dd == 3) { // top
          top_mp_ij[i].push_back(j);
        } else if (dd == 1) { // bottom
          bot_mp_ij[i].push_back(j);
        } else if (dd == 2) { // left
          left_mp_ji[j].push_back(i);
        } else { // right
          right_mp_ji[j].push_back(i);
        }
        continue;
      }
      if (seen[ni][nj]) continue;
      self(ni, nj);
    }
  };

  auto get_peri = [&](map<int, vector<int>> &mp) {
    for (auto &[_, a] : mp) {
      ranges::sort(a);
      for (int k = 0; k < ssize(a); k++) {
        if (k == 0 || a[k] != a[k-1]+1) peri++;
      }
    }
  };

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (seen[i][j]) continue;
      top_mp_ij.clear();
      bot_mp_ij.clear();
      left_mp_ji.clear();
      right_mp_ji.clear();
      area = peri = 0;
      solve(i, j);
      get_peri(top_mp_ij);
      get_peri(bot_mp_ij);
      get_peri(left_mp_ji);
      get_peri(right_mp_ji);
      ans += area*peri;
    }
  }

  cout << ans << '\n';

  return 0;
}
