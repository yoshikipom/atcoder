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
  int N, M, X, Y;
  cin >> N >> M >> X >> Y;
  vector<int> v_x, v_y;
  rep(i, N) {
    int x;
    cin >> x;
    v_x.push_back(x);
  }
  rep(i, M) {
    int y;
    cin >> y;
    v_y.push_back(y);
  }

  bool war = false;

  if (!(X < Y)) {
    war = true;
  }

  sort(v_x.begin(), v_x.end());
  sort(v_y.begin(), v_y.end());

  if (!(v_x[N - 1] < v_y[0] && X < v_y[0] && v_x[N - 1] < Y)) {
    war = true;
  }

  if (war) {
    cout << "War" << endl;
  } else {
    cout << "No War" << endl;
  }
  return 0;
}
