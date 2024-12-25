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

  int best_len = 0, current = 0;
  vector<string> ans;

  for (auto &u : a) {
    // cout << "Progress: " << ++current << endl;
    auto vs = vector(all(mp[u]));
    for (int mask = 1; mask < (1<<sze(vs)); mask++) {
      int m = mask, score = popcount((unsigned)m), ok = true;
      vector<string> clique{ u };
      while (m) {
        int v = __lg(lso(m));
        clique.push_back(vs[v]);
        m -= lso(m);
      }
      for (auto &u : clique) {
        for (auto &v : clique) {
          if (u == v) continue;
          if (!mp[u].contains(v)) {
            ok = false;
            break;
          }
        }
      }
      if (ok && score > best_len) {
        best_len = score;
        ans = clique;
      }
    }
  }

  R::sort(ans);

  string final_ans;

  for (int i : rng(sze(ans))) {
    if (i) final_ans += ',';
    final_ans += ans[i];
  }

  cout << final_ans << '\n';

  return 0;
}
