#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;

constexpr int DI = 4;

array<int, DI> di{ 0, 1, 0, -1 };
array<int, DI> dj{ 1, 0, -1, 0 };

string line;
int n, m;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) {
    g.push_back(line), m = ssize(line);
  }

  n = ssize(g);

  set<ii> peaks;
  vector seen(n, vector<int>(m, 0));

  int ans = 0;

  auto in_bounds = [&](int i, int j) -> bool {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  auto solve = [&](auto &&self, int ci, int cj, int cu) -> void {
    if (cu == 9) {
      peaks.insert({ ci, cj });
      return;
    }
    for (int dd = 0; dd < DI; dd++) {
      int ni = ci+di[dd], nj = cj+dj[dd];
      if (!in_bounds(ni, nj) || g[ni][nj]-'0' != cu+1) continue;
      self(self, ni, nj, cu+1);
    }
  };

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == '0') {
        peaks.clear();
        solve(solve, i, j, 0);
        ans += ssize(peaks);
      }
    }
  }

  cout << ans << '\n';

  return 0;
}
