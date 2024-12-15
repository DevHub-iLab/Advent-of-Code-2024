#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;

string line;
bool read_grid = true;
int n, m, sti, stj;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  vector<string> g;
  string s;

  while (getline(cin, line)) {
    if (empty(line)) n = ssize(g), read_grid = false;
    if (read_grid) {
      string tmp;
      for (auto &c : line) {
        if (c == '@') tmp += "@.";
        else if (c == 'O') tmp += "[]";
        else tmp += c, tmp += c;
      }
      g.push_back(tmp), m = ssize(tmp);
    } else {
      s += line;
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == '@') sti = i, stj = j;
    }
  }

  // for (int i = 0; i < n; i++) {
  //   for (int j = 0; j < m; j++) {
  //     cout << g[i][j];
  //   }
  //   cout << '\n';
  // }
  // cout << '\n';

  int ci = sti, cj = stj;

  for (auto &c : s) {
    int di = 0, dj = 0;
    switch (c) {
      case '<':
        di = 0, dj = -1;
        break;
      case '>':
        di = 0, dj = +1;
        break;
      case '^':
        di = -1, dj = 0;
        break;
      case 'v':
        di = +1, dj = 0;
        break;
    }

    bool found = true;
    set<ii> affected;
    vector<ii> resolve;
    queue<ii> q;

    q.push({ ci, cj });
    affected.insert({ ci, cj });
    resolve.push_back({ ci, cj });

    while (!empty(q) && found) {
      int qsize = ssize(q);
      for (int i = 0; i < qsize; i++) {
        auto [ci, cj] = q.front();
        q.pop();
        if (g[ci+di][cj+dj] == '[' || g[ci+di][cj+dj] == ']') {
          if (di != 0) {
            if (g[ci+di][cj+dj] == '[') {
              if (!affected.contains({ ci+di, cj+dj+1 })) {
                affected.insert({ ci+di, cj+dj+1 });
                resolve.push_back({ ci+di, cj+dj+1 });
                q.push({ ci+di, cj+dj+1 });
              }
            } else {
              if (!affected.contains({ ci+di, cj+dj-1 })) {
                affected.insert({ ci+di, cj+dj-1 });
                resolve.push_back({ ci+di, cj+dj-1 });
                q.push({ ci+di, cj+dj-1 });
              }
            }
          }
          if (!affected.contains({ ci+di, cj+dj })) {
            affected.insert({ ci+di, cj+dj });
            resolve.push_back({ ci+di, cj+dj });
            q.push({ ci+di, cj+dj });
          }
        } else if (g[ci+di][cj+dj] == '#') {
          found = false;
          break;
        }
      }
    }

    if (found) {
      ci += di, cj += dj;
      for (int i = ssize(resolve)-1; i >= 0; i--) {
        auto [ci, cj] = resolve[i];
        swap(g[ci][cj], g[ci+di][cj+dj]);
      }
    }

    // cout << "c: " << c << '\n';
    // for (int i = 0; i < n; i++) {
    //   for (int j = 0; j < m; j++) {
    //     cout << g[i][j];
    //   }
    //   cout << '\n';
    // }
    // cout << '\n';
  }

  ll ans = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (g[i][j] == '[') {
        ans += 100*i + j;
      }
    }
  }

  cout << ans << '\n';

  return 0;
}
