#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;
using ii = array<int, 2>;

int n;
string line;
constexpr int MAXI = 103, MAXJ = 101;
// constexpr int MAXI = 7, MAXJ = 11;

vector<ii> pos, vel;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);

  while (getline(cin, line)) {
    char _;
    int x, y;
    vector<string> parsed_eq = line
      | views::split("="sv)
      | ranges::to<vector<string>>();
    stringstream ss(parsed_eq[1]);
    ss >> x >> _ >> y;
    pos.push_back({ y, x });
    stringstream ss_new(parsed_eq[2]);
    ss_new >> x >> _ >> y;
    vel.push_back({ y, x });
    n++;
  }

  vector g(MAXI, vector(MAXJ, 0));

  for (int i = 0; i < n; i++) {
    int ni = (pos[i][0] + 100*vel[i][0])%MAXI;
    int nj = (pos[i][1] + 100*vel[i][1])%MAXJ;

    if (ni < 0) ni = (ni+MAXI)%MAXI;
    if (nj < 0) nj = (nj+MAXJ)%MAXJ;

    g[ni][nj]++;
  }

  ll q1 = 0, q2 = 0, q3 = 0, q4 = 0;

  for (int i = 0; i < MAXI; i++) {
    if (i == MAXI/2) continue;
    for (int j = 0; j < MAXJ; j++) {
      if (j == MAXJ/2) continue;
      if (i < MAXI/2 && j < MAXJ/2) q1 += g[i][j];
      if (i < MAXI/2 && j > MAXJ/2) q2 += g[i][j];
      if (i > MAXI/2 && j < MAXJ/2) q3 += g[i][j];
      if (i > MAXI/2 && j > MAXJ/2) q4 += g[i][j];
    }
  }

  cout << q1*q2*q3*q4 << '\n';

  return 0;
}
