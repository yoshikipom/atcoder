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

// 初期位置も座標に加える
// ソート
// 差のリストを作る セットにしとく
// 差の最大公約数を求める
int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}

int main() {
  int N, X;
  cin >> N >> X;
  vector<int> x;
  x.push_back(X);
  rep(i, N) {
    int xi;
    cin >> xi;
    x.push_back(xi);
  }

  sort(x.begin(), x.end());

  set<int> S;
  rep(i, N) {
    S.insert(x[i + 1] - x[i]);
    // cout << x[i + 1] - x[i] << endl;
  }
  auto it = S.begin();
  int result = *it;
  for (auto it = S.begin(), end = S.end(); it != end; ++it) {
    // cout << *it << endl;
    result = gcd(result, *it);
  }

  cout << result << endl;
  return 0;
}
