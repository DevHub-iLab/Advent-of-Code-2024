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

constexpr ll MOD = 16777216;
ll _;

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
  ll ans = 0;

  while (cin >> _) {
    a.push_back(_);
  }

  for (auto &i : a) {
    for (auto _ : rng(2'000)) {
      i = process(i);
    }
    ans += i;
  }

  cout << ans << '\n';

  return 0;
}
