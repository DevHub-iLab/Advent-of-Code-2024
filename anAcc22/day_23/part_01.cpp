#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;
namespace R = ranges;

auto rng(auto l, auto r) { assert(l <= r); return R::iota_view(l, r); }
auto RNG(auto l, auto r) { assert(l <= r); return R::iota_view(l, r+1); }
auto GNR(auto r, auto l) { return R::reverse_view(rng(l, r+1)); }
auto rng(auto r) { return rng(0, r); }

#define all(a) (a).begin(), (a).end()
#define ral(a) (a).rbegin(), (a).rend()
#define lso(x) ((x) & -(x))
#define sze(a) (int)ssize(a)

using ll = long long;

set<string> seen;
vector<string> a;
map<string, set<string>> mp;

string line;

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
    auto parsed = string_split(line, "-");
    string u = parsed[0], v = parsed[1];
    if (!seen.contains(u)) {
      seen.insert(u);
      a.push_back(u);
    }
    if (!seen.contains(v)) {
      seen.insert(v);
      a.push_back(v);
    }
    mp[u].insert(v);
    mp[v].insert(u);
  }

  int n = sze(a);

  vector<vector<string>> ans;

  for (int i : rng(n)) {
    for (auto u : mp[a[i]]) {
      for (auto v : mp[a[i]]) {
        if (u == v) continue;
        if (!mp[u].contains(v)) continue;
        if (a[i][0] == 't' || u[0] == 't' || v[0] == 't') {
          ans.push_back({ a[i], u, v });
        }
      }
    }
  }

  cout << sze(ans)/6 << '\n';

  return 0;
}
