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

bool isAcgt(string s) {
  for (char c : s) {
    if (c == 'A' || c == 'C' || c == 'G' || c == 'T') {
      continue;
    } else {
      return false;
    }
  }
  return true;
}

int main() {
  string s;
  cin >> s;

  int N = s.size();
  int longest = 0;

  rep(i, N) {
    for (int j = 0; i + j < N + 1; j++) {
      string sub = s.substr(i, j);
      if (isAcgt(sub)) {
        if (sub.size() > longest) {
          longest = sub.size();
        }
      }
    }
  }

  cout << longest << endl;
  return 0;
}
