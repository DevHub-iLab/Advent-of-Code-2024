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

mt19937 gen(chrono::steady_clock::now().time_since_epoch().count());

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
      outs.insert(out);
    }
  }

  auto itos = [&](int i) {
    string ans = to_string(i);
    if (sze(ans) == 1) ans = '0'+ans;
    return ans;
  };

  auto set_x_y = [&](ll x_val, ll y_val) -> void {
    for (int i : RNG(0, 44)) {
      string tar = 'x'+itos(i);
      if ((x_val>>i)&1) mp[tar] = 1;
      else mp[tar] = 0;
      tar = 'y'+itos(i);
      if ((y_val>>i)&1) mp[tar] = 1;
      else mp[tar] = 0;
    }
  };

  vector<string> a(all(outs));

  auto attempt = [&](ll x, ll y) -> bool {
    set_x_y(x, y);
    ll desired = x+y;
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
    for (int i : RNG(0, 44)) {
      if (((ans>>i)&1) != ((desired>>i)&1)) {
        cout << "i: " << i << '\n';
      }
    }
    return ans == desired;
  };

  set<string> invalid;

  // Credits: https://www.reddit.com/r/adventofcode/comments/1hl698z/2024_day_24_solutions/

  for (auto out : a) {
    int op = mp_main[out].second;
    auto [u, v] = mp_main[out].first;
    set<char> xyz{ 'x', 'y', 'z' };
    if (out[0] == 'z' && op != XOR && out != "z45") invalid.insert(out);
    if (op == XOR && !xyz.contains(out[0]) && !xyz.contains(u[0]) && !xyz.contains(v[0])) {
      invalid.insert(out);
    }
    if (op == XOR) {
      for (auto out_nxt : a) {
        int op = mp_main[out_nxt].second;
        auto [u, v] = mp_main[out_nxt].first;
        if ((out == u || out == v) && op == OR) invalid.insert(out);
      }
    }
    if (op == AND && u != "x00" && v != "x00") {
      for (auto out_nxt : a) {
        int op = mp_main[out_nxt].second;
        auto [u, v] = mp_main[out_nxt].first;
        if ((out == u || out == v) && op != OR) invalid.insert(out);
      }
    }
  }

  string ans;

  for (auto &s : invalid) {
    if (!empty(ans)) ans += ',';
    ans += s;
  }

  cout << ans << '\n';
}
