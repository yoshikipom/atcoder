#include <algorithm>
#include <cmath>
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
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int mod = 1e9 + 7;

  int N;
  string s;
  cin >> N;
  cin >> s;

  map<char, ll> m;
  for (char c : s) {
    if (m.count(c) == 0) {
      m[c] = 1;
    } else {
      m[c]++;
    }
  }

  int result = 1;
  for (auto it = m.begin(), end = m.end(); it != end; ++it) {
    result = (result * (1 + it->second)) % mod;
  }
  result -= 1;

  cout << result % mod << endl;

  return 0;
}
