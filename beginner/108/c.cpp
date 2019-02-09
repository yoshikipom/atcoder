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
  int N, K;
  cin >> N >> K;
  int a, b, c;
  ll count = 0;
  ll count2 = 0;
  if (K % 2 == 0) {
    // even
    count = N / K;
    count2 = N / (K / 2) - N / K;
    cout << count * count * count + count2 * count2 * count2 << endl;
  } else {
    // odd
    count = N / K;
    cout << count * count * count << endl;
  }
  return 0;
}
