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
  string ans = "";
  int N;
  cin >> N;
  if (N == 0) {
    cout << 0 << endl;
    return 0;
  }

  while (N != 0) {
    int rem = N % -2;
    N /= -2;

    if (rem < 0) {
      rem += 2;
      N++;
    }

    ans = (char)(rem + '0') + ans;
  }
  cout << ans << endl;
  return 0;
}
