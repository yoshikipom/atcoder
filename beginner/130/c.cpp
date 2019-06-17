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
  long double w, h, x, y;
  cin >> w >> h >> x >> y;

  cout << w * h * 1.0 / 2 << " ";

  if (x * 2 == w && y * 2 == h) {
    cout << 1 << endl;
  } else {
    cout << 0 << endl;
  }

  return 0;
}
