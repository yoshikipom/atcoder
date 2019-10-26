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
  ll L, R;
  cin >> L >> R;

  if (R - L > 2019) {
    cout << 0 << endl;
    return 0;
  }

  L = L % 2019;
  R = R % 2019;

  // cout << L << " " << R << endl;

  int result = INF;
  for (int i = L; i <= R; i++) {
    for (int j = i + 1; j <= R; j++) {
      result = min(result, i * j % 2019);
    }
  }

  cout << result << endl;

  return 0;
}
