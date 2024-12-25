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
using Input = pair<pair<string, string>, int>;

enum { AND, OR, XOR };

string line;
map<string, int> mp;
bool first_section = true;
map<string, Input> mp_main;

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

  set<string> outs;

  while (getline(cin, line)) {
    if (empty(line)) {
      first_section = false;
      continue;
    }
    if (first_section) {
      auto parsed = string_split(line, ": ");
      mp[parsed[0]] = stoi(parsed[1]);
    } else {
      auto parsed = string_split(line, " ");
      string u = parsed[0], v = parsed[2], out = parsed[4], op = parsed[1];
      int op_int = op == "AND" ? AND : op == "OR" ? OR : XOR;
      mp_main[out] = { { u, v }, op_int };
      outs.insert(u), outs.insert(v), outs.insert(out);
    }
  }

  vector<string> a(all(outs));
  set<string> seen;

  auto solve = [&](this auto self, string out) -> void {
    seen.insert(out);

    if (!mp_main.contains(out)) return;

    string u = mp_main[out].first.first;
    string v = mp_main[out].first.second;
    int op_type = mp_main[out].second;

    if (!seen.contains(u)) self(u);
    if (!seen.contains(v)) self(v);

    if (op_type == AND) mp[out] = mp[u]&mp[v];
    if (op_type == OR)  mp[out] = mp[u]|mp[v];
    if (op_type == XOR) mp[out] = mp[u]^mp[v];
  };

  for (auto &s : a) {
    if (seen.contains(s)) continue;
    solve(s);
  }

  ll ans = 0;

  for (auto &s : a) {
    if (s[0] == 'z') {
      string _ = s.substr(1);
      int pos = stoi(_);
      if (mp[s]) ans |= (1LL<<pos);
    }
  }

  cout << ans << '\n';

  return 0;
}
