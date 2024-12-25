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
using ii = array<int, 2>;
using cc = pair<char, char>;

map<cc, set<string>> mp_main, mp_side;
map<char, ii> mp_ctp_main, mp_ctp_side;
map<ii, set<string>> combis;

constexpr int LAYERS = 3;

vector<char> c_main{ 'A', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
vector<char> c_side{ 'A', '^', '<', 'v', '>' };

string line;
vector<int> best_lengths;
vector<string> inputs;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  while (getline(cin, line)) {
    inputs.push_back(line);
  }

  mp_ctp_main['7'] = { 0, 0 };
  mp_ctp_main['8'] = { 0, 1 };
  mp_ctp_main['9'] = { 0, 2 };
  mp_ctp_main['4'] = { 1, 0 };
  mp_ctp_main['5'] = { 1, 1 };
  mp_ctp_main['6'] = { 1, 2 };
  mp_ctp_main['1'] = { 2, 0 };
  mp_ctp_main['2'] = { 2, 1 };
  mp_ctp_main['3'] = { 2, 2 };
  mp_ctp_main['0'] = { 3, 1 };
  mp_ctp_main['A'] = { 3, 2 };

  mp_ctp_side['A'] = { 0, 2 };
  mp_ctp_side['^'] = { 0, 1 };
  mp_ctp_side['<'] = { 1, 0 };
  mp_ctp_side['v'] = { 1, 1 };
  mp_ctp_side['>'] = { 1, 2 };

  for (int i : RNG(-3, 3)) {
    for (int j : RNG(-3, 3)) {
      string base;
      if (j < 0) base += string(abs(j), '<');
      if (j > 0) base += string(j, '>');
      if (i < 0) base += string(abs(i), '^');
      if (i > 0) base += string(i, 'v');
      R::sort(base);
      set<string> ans;
      do {
        ans.insert(base);
      } while (next_permutation(all(base)));
      combis[{ i, j }] = ans;
    }
  }

  for (auto u : c_main) {
    for (auto v : c_main) {
      int di = mp_ctp_main[v][0]-mp_ctp_main[u][0];
      int dj = mp_ctp_main[v][1]-mp_ctp_main[u][1];
      mp_main[{ u, v }] = combis[{ di, dj }];
      if (u == '7' && v == '0') mp_main[{ u, v }].erase("vvv>");
      if (u == '7' && v == 'A') mp_main[{ u, v }].erase("vvv>>");
      if (u == '4' && v == '0') mp_main[{ u, v }].erase("vv>");
      if (u == '4' && v == 'A') mp_main[{ u, v }].erase("vv>>");
      if (u == '1' && v == '0') mp_main[{ u, v }].erase("v>");
      if (u == '1' && v == 'A') mp_main[{ u, v }].erase("v>>");
      if (u == '0' && v == '1') mp_main[{ u, v }].erase("<^");
      if (u == '0' && v == '4') mp_main[{ u, v }].erase("<^^");
      if (u == '0' && v == '7') mp_main[{ u, v }].erase("<^^^");
      if (u == 'A' && v == '1') mp_main[{ u, v }].erase("<<^");
      if (u == 'A' && v == '4') mp_main[{ u, v }].erase("<<^^");
      if (u == 'A' && v == '7') mp_main[{ u, v }].erase("<<^^^");
    }
  }

  for (auto u : c_side) {
    for (auto v : c_side) {
      int di = mp_ctp_side[v][0]-mp_ctp_side[u][0];
      int dj = mp_ctp_side[v][1]-mp_ctp_side[u][1];
      mp_side[{ u, v }] = combis[{ di, dj }];
      if (u == '<' && v == '^') mp_side[{ u, v }].erase("^>");
      if (u == '<' && v == 'A') mp_side[{ u, v }].erase("^>>");
      if (u == '^' && v == '<') mp_side[{ u, v }].erase("<v");
      if (u == 'A' && v == '<') mp_side[{ u, v }].erase("<<v");
    }
  }

  auto solve = [&](const string &base) {
    string root = 'A'+base;
    vector<string> raw_main, raw_filtered;

    auto build_main = [&](this auto self, int i = 1, string cur = "") -> void {
      if (i == sze(root)) raw_main.push_back(cur);
      char u = root[i-1], v = root[i];
      for (const auto &s : mp_main[{ u, v }]) {
        self(i+1, cur+s+'A');
      }
    };

    build_main();

    int mn_len = INT_MAX;

    for (const auto &s : raw_main) mn_len = min(mn_len, sze(s));
    for (const auto &s : raw_main) {
      if (sze(s) != mn_len) continue;
      raw_filtered.push_back(s);
    }

    set<string> best = set(all(raw_filtered));

    for (int _ : RNG(2, 3)) {
      set<string> raw;
      for (const auto &s : best) {
        string root = 'A'+s;
        auto build_side = [&](this auto self, int i = 1, string cur = "") -> void {
          if (i == sze(root)) raw.insert(cur);
          char u = root[i-1], v = root[i];
          for (const auto &s : mp_side[{ u, v }]) {
            self(i+1, cur+s+'A');
          }
        };
        build_side();
      }
      int mn_len = INT_MAX;
      for (const auto &s : raw) mn_len = min(mn_len, sze(s));
      best.clear();
      for (const auto &s : raw) {
        if (sze(s) != mn_len) continue;
        best.insert(s);
      }
    }

    return sze(*begin(best));
  };

  ll ans = 0;

  for (int i : rng(sze(inputs))) {
    best_lengths.push_back(solve(inputs[i]));
    string _ = inputs[i];
    _.pop_back();
    ans += stoll(_)*best_lengths.back();
  }

  cout << ans << '\n';

  return 0;
}
