#include <bits/stdc++.h>
#include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line, program_raw;
int a = -1, b = -1, c = -1;
bool read_prog = false;

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

  vector<int> program;

  while (getline(cin, line)) {
    if (empty(line)) continue;
    auto parsed = string_split(line, " ");
    if (!read_prog) {
      if (a == -1) a = stoi(parsed[2]);
      else if (b == -1) b = stoi(parsed[2]);
      else c = stoi(parsed[2]), read_prog = true;
    } else {
      program_raw = parsed[1];
      vector<string> prog_string = string_split(program_raw, ",");
      for (auto &s : prog_string) program.push_back(stoi(s));
      break;
    }
  }

  int n = ssize(program);

  // NOTE: <<- Input ->>
  // Register A: 32916674
  // Register B: 0
  // Register C: 0
  //
  // Program: 2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0

  auto solve = [&](ll a, ll b, ll c) -> vector<int> {
    int ins_ptr = 0, output_idx = 0;
    vector<int> output;
    while (ins_ptr < n) {
      int opcode = program[ins_ptr], operand = program[ins_ptr+1];
      ll combo = 0, jump_ptr = false, bad = false;
      switch (operand) {
        case 0:
          combo = 0;
          break;
        case 1:
          combo = 1;
          break;
        case 2:
          combo = 2;
          break;
        case 3:
          combo = 3;
          break;
        case 4:
          combo = a;
          break;
        case 5:
          combo = b;
          break;
        case 6:
          combo = c;
          break;
        case 7: // WARN: shouldn't appear...
          break;
      }
      switch (opcode) {
        case 0:
          a = a/(1LL<<combo);
          break;
        case 1:
          b = b^operand;
          break;
        case 2:
          b = combo%8;
          break;
        case 3:
          if (a != 0) {
            jump_ptr = true;
            ins_ptr = operand;
          }
          break;
        case 4:
          b = b^c;
          break;
        case 5:
          output.push_back(combo%8);
          if (output_idx >= n) bad = true;
          // if (output[output_idx] != program[output_idx]) bad = true;
          output_idx++;
          break;
        case 6:
          b = a/(1LL<<combo);
          break;
        case 7:
          c = a/(1LL<<combo);
          break;
      }
      if (!jump_ptr) ins_ptr += 2;
      if (bad) break;
    }
    return output;
  };

  ll ans = 0;

  auto pray = [&](this auto &&self, int i, ll cur) -> void {
    if (i == -1) {
      if (ans == 0) ans = cur;
      return;
    }
    for (ll m = 0; m < 8; m++) {
      auto output = solve(cur|(m<<(3*i)), b, c);
      if (ssize(output) == ssize(program) && output[i] == program[i]) {
        self(i-1, cur|(m<<(3*i)));
      }
    }
  };

  pray(15, 0);

  cout << "ans: " << ans << '\n';

  fmt::print("{}\n", solve(ans, b, c));
  fmt::print("{}\n", program);

  return 0;
}
