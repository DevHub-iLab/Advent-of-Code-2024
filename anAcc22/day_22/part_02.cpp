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

using ll   = long long;
using iiii = array<int, 4>;

constexpr ll MOD = 16777216;
ll _;

int n;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  auto mix = [](ll x, ll y) { return x^y; };
  auto prune = [&](ll x) { return x%MOD; };

  auto process = [&](ll secret) -> ll {
    secret = prune(mix(64*secret, secret));
    secret = prune(mix(secret/32, secret));
    secret = prune(mix(2048*secret, secret));
    return secret;
  };

  vector<ll> a;
  vector<vector<int>> b;
  vector<vector<int>> c;

  while (cin >> _) {
    a.push_back(_);
  }

  n = sze(a);

  for (auto &i : a) {
    b.push_back({});
    c.push_back({});
    vector<int> raw{ (int)(i%10) };
    for (auto _ : rng(2'000)) {
      i = process(i);
      raw.push_back((int)(i%10));
    }
    for (auto i : RNG(1, 2'000)) {
      b.back().push_back(raw[i]-raw[i-1]);
      c.back().push_back(raw[i]);
    }
  }

  set<iiii> seq;

  for (auto &a : b) {
    for (int i : rng(0, 2'000-3)) {
      seq.insert({ a[i], a[i+1], a[i+2], a[i+3] });
    }
  }

  vector<map<iiii, int>> mp(n);
  map<iiii, ll> mp_main;

  for (int i : rng(n)) {
    for (int j : rng(2'000-3)) {
      iiii seq = { b[i][j], b[i][j+1], b[i][j+2], b[i][j+3] };
      if (!mp[i].contains(seq)) {
        mp[i][seq] = c[i][j+3];
        mp_main[seq] += mp[i][seq];
      }
    }
  }

  ll ans = 0;

  for (auto &s : seq) {
    ans = max(ans, mp_main[s]);
  }

  cout << ans << '\n';

  return 0;
}
