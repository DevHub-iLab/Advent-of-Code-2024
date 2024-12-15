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

  map<pair<ii, ii>, bool> seen;

  for (auto &[_, cs] : mp) {
    for (int i = 0; i < ssize(cs); i++) {
      for (int j = i+1; j < ssize(cs); j++) {
        gcpy[cs[i][0]][cs[i][1]] = '!';
        gcpy[cs[j][0]][cs[j][1]] = '!';

        int dx = cs[j][0] - cs[i][0];
        int dy = cs[j][1] - cs[i][1];

        if (seen[{ ii{ cs[i][0], cs[i][1] }, ii{ dx, dy } }]) continue;
        if (seen[{ ii{ cs[i][0], cs[i][1] }, ii{ -dx, -dy } }]) continue;
        if (seen[{ ii{ cs[j][0], cs[j][1] }, ii{ dx, dy } }]) continue;
        if (seen[{ ii{ cs[j][0], cs[j][1] }, ii{ -dx, -dy } }]) continue;

        seen[{ ii{ cs[i][0], cs[i][1] }, ii{ dx, dy } }] = true;
        seen[{ ii{ cs[j][0], cs[j][1] }, ii{ dx, dy } }] = true;

        seen[{ ii{ cs[i][0], cs[i][1] }, ii{ -dx, -dy } }] = true;
        seen[{ ii{ cs[j][0], cs[j][1] }, ii{ -dx, -dy } }] = true;

        int ni, nj;

        ni = cs[j][0]+dx, nj = cs[j][1]+dy;
        while (ok(ni, nj)) {
          seen[{ ii{ ni, nj }, ii{ dx, dy } }] = true;
          seen[{ ii{ ni, nj }, ii{ -dx, -dy } }] = true;
          gcpy[ni][nj] = '!';
          ni += dx, nj += dy;
        }

        ni = cs[i][0]-dx, nj = cs[i][1]-dy;
        while (ok(ni, nj)) {
          seen[{ ii{ ni, nj }, ii{ dx, dy } }] = true;
          seen[{ ii{ ni, nj }, ii{ -dx, -dy } }] = true;
          gcpy[ni][nj] = '!';
          ni -= dx, nj -= dy;
        }
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
