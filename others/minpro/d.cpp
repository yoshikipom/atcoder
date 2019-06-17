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
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; ++i) cin >> a[i];

  vector<long long> dp(5, 0);
  for (int i = 0; i < n; ++i) {
    vector<long long> nextDp(5, INF);
    long long tmp = dp[0];
    nextDp[0] = tmp + a[i];

    tmp = min(tmp, dp[1]);
    nextDp[1] = tmp + (a[i] == 0 ? 2 : a[i] % 2);

    tmp = min(tmp, dp[2]);
    nextDp[2] = tmp + ((a[i] + 1) % 2);

    tmp = min(tmp, dp[3]);
    nextDp[3] = tmp + (a[i] == 0 ? 2 : a[i] % 2);

    tmp = min(tmp, dp[4]);
    nextDp[4] = tmp + a[i];

    dp = move(nextDp);
  }

  long long ans = *min_element(dp.begin(), dp.end());
  cout << ans << endl;

  return 0;
}
