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

  getline(cin, line);

  vector<string> tows = string_split(line, ", ");

  getline(cin, line); // NOTE: empty line

  int ans = 0;

  while (getline(cin, line)) {
    int n = sze(line);
    vector<int> dp(n+1, INT_MAX);
    dp[0] = 0;
    for (auto i : rng(1, n, 1)) {
      for (const string &s : tows) {
        if (sze(s) > i) continue;
        bool ok = true;
        for (auto k : rng(sze(s))) {
          if (line[i-sze(s)+k] != s[k]) ok = false;
        }
        if (ok && dp[i-sze(s)] != INT_MAX) {
          dp[i] = min(dp[i], dp[i-sze(s)]+1);
        }
      }
    }
    if (dp[n] != INT_MAX) ans++;
  }

  cout << ans << '\n';

  return 0;
}
