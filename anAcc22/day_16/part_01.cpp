#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;
using Node = pair<pair<ll, int>, ii>;

constexpr int DI = 4;

array<int, DI> di{ 0, 1, 0, -1 };
array<int, DI> dj{ 1, 0, -1, 0 };

int n, m;

string line;
int sti, stj, eni, enj;

constexpr ll INF = 1'000'000'000'000'000'000;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;

  while (getline(cin, line)) {
    g.push_back(line), m = ssize(line);
  }

  n = ssize(g);

  vector dist(n, vector(m, vector(4, INF)));

  for (int i = 0; i < n ; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == 'S') sti = i, stj = j;
      if (g[i][j] == 'E') eni = i, enj = j;
    }
  }

  priority_queue<Node, vector<Node>, greater<Node>> pq;
  pq.push({ { 0, 0 }, ii{ sti, stj } });
  dist[sti][stj][0] = 0;

  auto in_bounds = [&](int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
  };

  auto mod = [](int x, int m) -> int {
    return (x%m + m)%m;
  };

  while (!empty(pq)) {
    auto [dist_dir, coords] = pq.top();

    auto [cd, dd] = dist_dir;
    auto [ci, cj] = coords;

    pq.pop();
    if (cd != dist[ci][cj][dd]) continue;

    for (auto &__ : { -1, 1 }) {
      int new_dd = mod(dd+__, 4);
      if (dist[ci][cj][new_dd] <= dist[ci][cj][dd]+1'000) continue;
      dist[ci][cj][new_dd] = dist[ci][cj][dd]+1'000;
      pq.push({ { dist[ci][cj][new_dd], new_dd }, ii{ ci, cj } });
    }
    int ni = ci+di[dd], nj = cj+dj[dd];
    if (!in_bounds(ni, nj) || g[ni][nj] == '#') continue;
    if (dist[ni][nj][dd] <= dist[ci][cj][dd]+1) continue;
    dist[ni][nj][dd] = dist[ci][cj][dd]+1;
    pq.push({ { dist[ni][nj][dd], dd }, ii{ ni, nj } });
  }

  cout << *min_element(begin(dist[eni][enj]), end(dist[eni][enj])) << '\n';

  return 0;
}
