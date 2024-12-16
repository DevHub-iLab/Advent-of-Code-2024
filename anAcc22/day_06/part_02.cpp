#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

constexpr int DI = 4;

array<int, DI> di{ -1, 0, 1, 0 };
array<int, DI> dj{ 0, 1, 0, -1 };

string line;
vector<string> g;
int n, m, si, sj, cd = 0;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  while (getline(cin, line)) {
    g.push_back(line);
  }

  n = ssize(g), m = ssize(g[0]);

  auto ok = [&](int i, int j) -> bool {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == '^') si = i, sj = j;
    }
  }

  auto solve = [&](auto &&self, int ci, int cj) -> void {
    g[ci][cj] = 'X';
    int ni = ci+di[cd], nj = cj+dj[cd];
    if (!ok(ni, nj)) return;
    if (g[ni][nj] == '#') {
      cd = (cd+1)%4;
      self(self, ci, cj);
    } else {
      self(self, ni, nj);
    }
  };

  solve(solve, si, sj);

  int ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == 'X' && (i != si|| j != sj)) {
        g[i][j] = '#';
        vector cnt(n, vector(m, vector(4, 0)));
        bool is_loop = false;
        cd = 0;
        auto solve = [&](auto &&self, int ci, int cj) -> void {
          if (!is_loop && cnt[ci][cj][cd]) {
            is_loop = true;
            return;
          }
          cnt[ci][cj][cd] = true;
          if (is_loop) return;
          int ni = ci+di[cd], nj = cj+dj[cd];
          if (!ok(ni, nj)) return;
          if (g[ni][nj] == '#') {
            cd = (cd+1)%4;
            self(self, ci, cj);
          } else {
            self(self, ni, nj);
          }
        };
        solve(solve, si, sj);
        g[i][j] = 'X';
        if (is_loop) ans++;
      }
    }
  }

  cout << ans << '\n';

  return 0;
}
