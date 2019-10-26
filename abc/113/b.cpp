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
  int N;
  float T, A;
  cin >> N >> T >> A;
  float H[N];
  rep(i, N) cin >> H[i];
  float result[N];
  rep(i, N) { result[i] = T - H[i] * 0.006; }
  float diff = INF;
  int index = 0;
  rep(i, N) {
    if (std::abs(result[i] - A) < diff) {
      diff = std::abs(result[i] - A);
      index = i;
    }
    // cout << diff << endl;
    // cout << std::abs(result[i] - A) << endl;
    // cout << index << endl;
  }
  cout << index + 1 << endl;
  return 0;
}
