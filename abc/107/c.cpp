#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
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
  int N, K;
  cin >> N >> K;
  vector<int> x1, x2;
  rep(i, N) {
    int x;
    cin >> x;
    if (x >= 0) {
      x2.push_back(x);
    } else if (x < 0) {
      x1.push_back(-x);
    } else {
      cout << "error" << endl;
    }
  }
  sort(x1.begin(), x1.end());

  int N1 = x1.size();
  int N2 = x2.size();
  int result = INF;
  rep(i, K + 1) {
    // cout << i << " " << result << endl;
    int K1 = i;
    int K2 = K - i;
    if (K1 > N1 || K2 > N2) {
      // cout << "n1" << endl;
      continue;
    }
    if (K2 == 0) {
      // cout << "n2" << endl;
      result = min(result, x1[K1 - 1]);
      continue;
    }
    if (K1 == 0) {
      // cout << "n3" << endl;
      result = min(result, x2[K2 - 1]);
      continue;
    }
    // cout << "n4" << endl;
    int alpha = min(x1[K1 - 1], x2[K2 - 1]);
    result = min(result, x1[K1 - 1] + x2[K2 - 1] + alpha);
    continue;
  }

  cout << result << endl;

  return 0;
}
