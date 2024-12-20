#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;
namespace R = ranges;

auto rng(auto l, auto r, int o = false) { // NOTE: enabling 'o' implies <= 
  assert(l <= r); return R::iota_view(l, r+o);
}
auto gnr(auto r, auto l) { return R::reverse_view(rng(l, r+1)); }
auto rng(auto r) { return rng(0, r, false); }

#define all(a) (a).begin(), (a).end()
#define ral(a) (a).rbegin(), (a).rend()
#define lso(x) ((x) & -(x))
#define sze(a) (int)ssize(a)

using ll = long long;

constexpr int DI = 4;
constexpr int SKIP = 20;

array<int, DI> di{ 0, 1, 0, -1 };
array<int, DI> dj{ 1, 0, -1, 0 };

int n, m, sti, stj, eni, enj;
string line;

constexpr int INF = 1e9;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) {
    g.push_back(line), m = sze(line);
  }

  n = sze(g);

  vector dsta(n, vector(m, INF));
  vector dend(n, vector(m, INF));

  for (int i : rng(n)) {
    for (int j : rng(m)) {
      if (g[i][j] == 'S') sti = i, stj = j;
      if (g[i][j] == 'E') eni = i, enj = j;
    }
  }

  auto ok = [&](int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  int ci = sti, cj = stj;
  dsta[sti][stj] = 0;

  while (!(ci == eni && cj == enj)) {
    for (int dd : rng(DI)) {
      int ni = ci+di[dd], nj = cj+dj[dd];
      if (!ok(ni, nj) || g[ni][nj] == '#' || dsta[ni][nj] != INF) continue;
      dsta[ni][nj] = dsta[ci][cj]+1;
      ci = ni, cj = nj;
    }
  }

  ci = eni, cj = enj;
  dend[ci][cj] = 0;

  while (!(ci == sti && cj == stj)) {
    for (int dd : rng(DI)) {
      int ni = ci+di[dd], nj = cj+dj[dd];
      if (!ok(ni, nj) || g[ni][nj] == '#' || dend[ni][nj] != INF) continue;
      dend[ni][nj] = dend[ci][cj]+1;
      ci = ni, cj = nj;
    }
  }

  int tot = dsta[eni][enj];

  map<int, int> mp;

  for (int i : rng(n)) {
    for (int j : rng(m)) {
      if (dsta[i][j] == INF) continue;
      for (int ni : rng(i-SKIP, i+SKIP, 1)) {
        for (int nj : rng(j-SKIP, j+SKIP, 1)) {
          int skip_len = abs(ni-i)+abs(nj-j);
          if (skip_len > SKIP || !ok(ni, nj) || g[ni][nj] == '#') {
            continue;
          }
          int new_tot = dsta[i][j]+dend[ni][nj]+skip_len;
          if (new_tot >= tot) continue;
          mp[tot-new_tot]++;
        }
      }
    }
  }

  int ans = 0;

  for (auto &[k, cnt] : mp) {
    if (k >= 100) ans += cnt;
  }

  cout << ans << '\n';

  return 0;
}
