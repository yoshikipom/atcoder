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
  int x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  int x3 = x2 - (y2 - y1);
  int y3 = y2 + (x2 - x1);
  int x4 = x3 - (x2 - x1);
  int y4 = y3 - (y2 - y1);
  cout << x3 << " ";
  cout << y3 << " ";
  cout << x4 << " ";
  cout << y4 << " ";
  cout << endl;
  return 0;
}
