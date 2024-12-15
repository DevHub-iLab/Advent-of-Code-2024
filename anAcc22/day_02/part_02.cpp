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
    auto is_safe = [](vector<int> &a) -> bool {
      auto b = a;
      ranges::reverse(b);
      bool ok = is_sorted(begin(a), end(a)) || is_sorted(begin(b), end(b));
      for (int i = 1; i < ssize(a); i++) {
        if (abs(a[i-1]-a[i]) >= 4 || a[i-1] == a[i]) {
          ok = false;
        }
      }
      return ok;
    };
    bool ok = false;
    for (int i = 0; i < ssize(a); i++) {
      auto tmp = a;
      tmp.erase(begin(tmp)+i);
      if (is_safe(tmp)) ok |= true;
    }
    ans += ok;
  }

  cout << ans << '\n';

  return 0;
}
