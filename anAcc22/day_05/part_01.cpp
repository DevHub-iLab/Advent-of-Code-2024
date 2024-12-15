#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;

string line;
bool first_part = true;
int x, y, n;
char _;

vector<int> split(const string &s, char delim) {
  vector<int> ans;
  stringstream ss(s);
  string item;
  while (getline(ss, item, delim)) {
    ans.push_back(stoi(item));
  }
  return ans;
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<ii> rules;
  map<int, set<int>> rules_mp;
  ll ans = 0;

  while (getline(cin, line)) {
    if (empty(line)) { first_part = false; continue; }
    stringstream ss(line);
    if (first_part) {
      ss >> x >> _ >> y;
      rules.push_back({ x, y });
      rules_mp[x].insert(y);
    } else {
      auto a = split(line, ',');
      n = ssize(a);
      map<int, int> idx;
      for (int i = 0; i < n; i++) {
        idx[a[i]] = i;
      }
      bool ok = true;
      set<int> bad_idx_set;
      for (auto &[x, y] : rules) {
        if (idx.contains(x) && idx.contains(y) && idx[x] > idx[y]) {
          bad_idx_set.insert(x), bad_idx_set.insert(y);
          ok = false;
        }
      }
      if (!ok) {
        vector<int> bad_idx;
        for (int i = 0; i < n; i++) {
          if (bad_idx_set.contains(a[i])) bad_idx.push_back(i);
        }
        auto sorted_bad_idx = bad_idx;
        ranges::sort(sorted_bad_idx, [&](int i, int j) {
          return rules_mp[a[i]].contains(a[j]);
        });
        auto solved = a;
        for (int i = 0; i < ssize(bad_idx); i++) {
          solved[bad_idx[i]] = a[sorted_bad_idx[i]];
        }
        ans += solved[n/2];
      }
    }
  }

  cout << ans << '\n';

  return 0;
}
