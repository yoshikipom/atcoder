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
  int N, D;
  cin >> N >> D;

  int X[N][D];
  rep(i, N) {
    rep(j, D) { cin >> X[i][j]; }
  }

  int result = 0;
  rep(i, N) {
    for (int j = i + 1; j < N; j++) {
      double d = 0;
      rep(k, D) { d += pow(X[i][k] - X[j][k], 2); }
      d = sqrt(d);
      if (int(d) == d) {
        result++;
      }
    }
  }
  cout << result << endl;

  return 0;
}
