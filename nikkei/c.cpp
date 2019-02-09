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
typedef long long ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int N;
  vector<int> A, B;
  // a+bとindexのpair
  vector<pair<int, int>> P;
  ll result = 0;
  cin >> N;
  rep(i, N) {
    // cout << i << endl;
    int a, b, c;
    cin >> a >> b;
    A.push_back(a);
    B.push_back(b);
    result -= b;
    P.push_back(make_pair(a, b));
  }
  sort(all(P),
       [](auto x, auto y) { return x.first + x.second > y.first + y.second; });

  rep(i, N) {
    if (i % 2 == 0) {
      // turn for A
      result += P[i].first + P[i].second;
    } else {
      // turn for B
      // result -= B[P[i].second];
    }
  }
  cout << result << endl;

  return 0;
}
