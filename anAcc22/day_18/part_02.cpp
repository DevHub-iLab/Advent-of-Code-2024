#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;
namespace R = ranges;

auto rng(auto l, auto r, int o = false) { return R::iota_view(l, r+o); }
auto gnr(auto r, auto l) { return R::reverse_view(R::iota_view(l, r+1)); }
auto rng(auto r, int o = false) { return rng(0, r, o); }

#define all(a) (a).begin(), (a).end()
#define lso(x) ((x) & -(x))
#define sz(a) (int)ssize(a)

using ll = long long;
using ii = array<int, 2>;

string line;
vector<ii> cods;

constexpr int DI = 4;

array<int, DI> di{ 0, 1, 0, -1 };
array<int, DI> dj{ 1, 0, -1, 0 };

constexpr int LEN = 70;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  auto string_split = [](const string &s, const string &delims) {
    size_t prv = 0, pos;
    vector<string> parsed;
    while ((pos = s.find_first_of(delims, prv)) != string::npos) {
      if (pos > prv) parsed.push_back(s.substr(prv, pos-prv));
      prv = pos+1;
    }
    if (prv < size(s)) parsed.push_back(s.substr(prv, string::npos));
    return parsed;
  };

  while (getline(cin, line)) {
    auto parsed = string_split(line, ",");
    int i = stoi(parsed[1]), j = stoi(parsed[0]);
    cods.push_back({ i, j });
  }

  // for (auto &s : g) cout << s << '\n';

  auto in_bounds = [&](int i, int j) {
    return 0 <= i && i <= LEN && 0 <= j && j <= LEN;
  };

  auto build = [&](const vector<string> &g) -> bool {
    vector dist(LEN+1, vector(LEN+1, INT_MAX));
    dist[0][0] = 0;
    queue<ii> q;
    q.push({ 0, 0 });
    while (sz(q)) {
      auto [ci, cj] = q.front();
      q.pop();
      for (auto dd : rng(4)) {
        int ni = ci+di[dd], nj = cj+dj[dd];
        if (!in_bounds(ni, nj) || g[ni][nj] == '#') continue;
        if (dist[ni][nj] != INT_MAX) continue;
        dist[ni][nj] = dist[ci][cj]+1;
        q.push({ ni, nj });
      }
    }
    return dist[LEN][LEN] != INT_MAX;
  };

  int lo = 0, hi = sz(cods)-1, mi, an = 0;

  while (lo <= hi) {
    mi = midpoint(lo, hi);
    vector g(LEN+1, string(LEN+1, '.'));
    for (auto i : rng(mi, 1)) {
      g[cods[i][0]][cods[i][1]] = '#';
    }
    bool status = build(g);
    if (status) an = mi, lo = mi+1;
    else hi = mi-1;
  }

  an++;
  cout << cods[an][1] << ',' << cods[an][0] << '\n';

  return 0;
}
