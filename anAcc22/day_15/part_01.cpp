#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
bool read_grid = true;
int n, m, sti, stj;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;
  string s;

  while (getline(cin, line)) {
    if (empty(line)) n = ssize(g), read_grid = false;
    if (read_grid) {
      g.push_back(line), m = ssize(line);
    } else {
      s += line;
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == '@') sti = i, stj = j;
    }
  }

  // for (int i = 0; i < n; i++) {
  //   for (int j = 0; j < m; j++) {
  //     cout << g[i][j];
  //   }
  //   cout << '\n';
  // }
  // cout << '\n';

  int ci = sti, cj = stj;

  for (auto &c : s) {
    int di = 0, dj = 0;
    switch (c) {
      case '<':
        di = 0, dj = -1;
        break;
      case '>':
        di = 0, dj = +1;
        break;
      case '^':
        di = -1, dj = 0;
        break;
      case 'v':
        di = +1, dj = 0;
        break;
    }
    bool found = false;
    int ni = ci, nj = cj, kf = 0;
    for (int k = 1;; k++) {
      ni = ci + k*di, nj = cj + k*dj;
      if (g[ni][nj] == '#') break;
      if (g[ni][nj] == '.') {
        found = true;
        kf = k;
        break;
      }
    }
    if (found) {
      ci += di, cj += dj;
      di *= -1, dj *= -1;
      for (int i = 0; i < kf; i++) {
        swap(g[ni][nj], g[ni + di][nj + dj]);
        ni += di, nj += dj;
      }
    }
    // cout << "c: " << c << '\n';
    // for (int i = 0; i < n; i++) {
    //   for (int j = 0; j < m; j++) {
    //     cout << g[i][j];
    //   }
    //   cout << '\n';
    // }
    // cout << '\n';
  }

  ll ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == 'O') {
        ans += 100*i + j;
      }
    }
  }

  cout << ans << '\n';

  return 0;
}
