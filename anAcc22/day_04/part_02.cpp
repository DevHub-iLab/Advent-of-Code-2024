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

  auto check = [&](int i, int j) -> bool {
    if (i == 0 || i == n-1 || j == 0 || j == m-1) return false;
    bool dd = (g[i-1][j-1] == 'M' && g[i+1][j+1] == 'S');
    dd |= (g[i-1][j-1] == 'S' && g[i+1][j+1] == 'M');
    bool du = (g[i-1][j+1] == 'M' && g[i+1][j-1] == 'S');
    du |= (g[i-1][j+1] == 'S' && g[i+1][j-1] == 'M');
    return dd && du;
  };

  int ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] != 'A') continue;
      ans += check(i, j);
    }
  }

  cout << ans << '\n';

  return 0;
}
