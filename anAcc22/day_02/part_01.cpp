#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
int x;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  int ans = 0;

  while (getline(cin, line)) {
    stringstream sstream(line);
    vector<int> a;
    while (sstream >> x) {
      a.push_back(x);
    }
    auto b = a;
    ranges::reverse(b);
    bool a_ok = is_sorted(begin(a), end(a)), b_ok = is_sorted(begin(b), end(b));
    bool ok = a_ok || b_ok;
    for (int i = 1; i < ssize(a); i++) {
      if (abs(a[i-1]-a[i]) >= 4 || a[i-1] == a[i]) {
        ok = false;
      }
    }
    ans += ok;
  }

  cout << ans << '\n';

  return 0;
}
