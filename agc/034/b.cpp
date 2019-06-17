#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

void strReplace(std::string& str, const std::string& from,
                const std::string& to) {
  std::string::size_type pos = 0;
  while (pos = str.find(from, pos), pos != std::string::npos) {
    str.replace(pos, from.length(), to);
    pos += to.length();
  }
}

vector<string> createSet(string s) {
  vector<string> az_set;
  string az = "";
  for (char c : s) {
    if (c == 'B' || c == 'C') {
      if (az.size() != 0) {
        az_set.push_back(az);
      }
      az = "";
    } else if (c == 'A' || c == 'Z') {
      az = az + c;
    }
  }
  if (az.size() != 0) {
    az_set.push_back(az);
  }

  return az_set;
}

int main() {
  string s;
  cin >> s;

  // BCをZに置換
  strReplace(s, "BC", "Z");

  // AとZのみでできた塊を見つける
  vector<string> az_set = createSet(s);

  // 全部の塊のZを左に寄せるのに何回操作するか計算する
  ll result = 0;
  for (string az : az_set) {
    ll sub_result = 0;
    ll a_count = 0;
    for (char c : az) {
      if (c == 'A') {
        a_count++;
      } else if (c == 'Z') {
        sub_result += a_count;
      }
    }
    // cout << *it << "の移動は" << sub_result << "回" << endl;
    result += sub_result;
  }

  cout << result << endl;

  return 0;
}
