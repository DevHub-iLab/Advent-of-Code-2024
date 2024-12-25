#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;
namespace R = ranges;

auto rng(auto l, auto r) {
  if (l <= r) return R::iota_view(l, r);
  return R::iota_view(l, l);
}
auto RNG(auto l, auto r) { return rng(l, r+1); }
auto GNR(auto r, auto l) { return R::reverse_view(rng(l, r+1)); }
auto rng(auto r) { return rng(0, r); }

#define all(a) (a).begin(), (a).end()
#define ral(a) (a).rbegin(), (a).rend()
#define sze(a) ((int)ssize(a))
#define lso(x) ((x) & -(x))

using ll = long long;

int n, m;
string line;
vector<string> tmp_g;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  auto convert_to_lock = [&]() {
    vector<int> ans;
    for (int j : rng(m)) {
      int len = 0;
      for (int i : rng(1, n)) {
        if (tmp_g[i][j] == '.') break;
        len++;
      }
      ans.push_back(len);
    }
    return ans;
  };

  auto convert_to_key = [&]() {
    vector<int> ans;
    for (int j : rng(m)) {
      int len = 0;
      for (int i : GNR(n-2, 0)) {
        if (tmp_g[i][j] == '.') break;
        len++;
      }
      ans.push_back(len);
    }
    return ans;
  };

  set<vector<int>> locks, keys;

  while (getline(cin, line)) {
    if (empty(line)) {
      n = sze(tmp_g), m = sze(tmp_g[0]);
      if (tmp_g[0][0] == '#') {
        locks.insert(convert_to_lock());
      } else {
        keys.insert(convert_to_key());
      }
      tmp_g.clear();
    } else {
      tmp_g.push_back(line);
    }
  }

  if (tmp_g[0][0] == '#') {
    locks.insert(convert_to_lock());
  } else {
    keys.insert(convert_to_key());
  }

  int ans = 0;

  for (auto &lock : locks) {
    for (auto &key : keys) {
      bool ok = true;
      for (int i : rng(m)) {
        if (lock[i]+key[i] > n-2) {
          ok = false;
          break;
        }
      }
      if (ok) ans++;
    }
  }

  cout << ans << '\n';

  return 0;
}
