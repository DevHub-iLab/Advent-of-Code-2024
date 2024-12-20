#include <bits/stdc++.h>
// #include <fmt/ranges.h> // WARN: remove before submission

using namespace std;

using ll = long long;

string line;
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
      string program_raw = parsed[1];
      vector<string> prog_string = string_split(program_raw, ",");
      for (auto &s : prog_string) program.push_back(stoi(s));
      break;
    }
  }

  int ins_ptr = 0, n = ssize(program);
  vector<int> output;

  while (ins_ptr < n) {
    int opcode = program[ins_ptr], operand = program[ins_ptr+1];
    int combo = 0, jump_ptr = false;
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
        a = a>>combo;
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
        break;
      case 6:
        b = a>>combo;
        break;
      case 7:
        c = a>>combo;
        break;
    }
    if (!jump_ptr) ins_ptr += 2;
  }

  string ans;

  for (auto &i : output) {
    if (empty(ans)) ans += to_string(i);
    else ans += ","+to_string(i);
  }

  cout << ans << "\n";

  return 0;
}
