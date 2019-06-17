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

int main() {
  int N;
  cin >> N;
  string s;
  cin >> s;

  int red = 0;
  int blue = 0;
  for (char c : s) {
    if (c == 'R') {
      red++;
    } else if (c == 'B') {
      blue++;
    } else {
      cout << "error" << endl;
    }
  }

  if (red > blue) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
