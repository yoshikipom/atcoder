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
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  ll K, A, B;
  cin >> K >> A >> B;

  ll N = 1;

  if (B - A > 2) {
    if (K >= A + 1) {
      // change YEN
      // beat
      N += A - 1;
      K -= A - 1;
      // change
      N += (K / 2) * (B - A);
      N += K % 2;
    } else {
      // No change
      N += K;
    }
  } else {
    N += K;
  }

  cout << N << endl;

  return 0;
}
