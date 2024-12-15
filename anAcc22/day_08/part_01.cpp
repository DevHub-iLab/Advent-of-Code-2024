#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;

string line;
int n, m;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) {
    g.push_back(line), m = ssize(line);
  }

  n = ssize(g);
  auto gcpy = g;

  map<char, vector<ii>> mp;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] != '.') {
        mp[g[i][j]].push_back({ i, j });
      }
    }
  }

  auto ok = [&](int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  for (auto &[_, coords] : mp) {
    for (int i = 0; i < ssize(coords); i++) {
      for (int j = i+1; j < ssize(coords); j++) {
        int dx = coords[j][0] - coords[i][0];
        int dy = coords[j][1] - coords[i][1];
        int ni, nj;
        ni = coords[j][0]+dx, nj = coords[j][1]+dy;
        if (ok(ni, nj)) gcpy[ni][nj] = '!';
        ni = coords[i][0]-dx, nj = coords[i][1]-dy;
        if (ok(ni, nj)) gcpy[ni][nj] = '!';
      }
    }
  }

  int ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      ans += (gcpy[i][j] == '!');
    }
  }

  cout << ans << '\n';

  return 0;
}
