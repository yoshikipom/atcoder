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
  int N;
  vector<int> A, B;
  vector<pair<int, int>> pairs(N);
  ll result = 0;
  cin >> N;
  rep(i, N) {
    // cout << i << endl;
    int a, b, c;
    cin >> a >> b;
    c = a + b;
    A.push_back(a);
    B.push_back(b);
    pairs.push_back(make_pair(c, i));
  }

  sort(pairs.begin(), pairs.end(),
       [](auto x, auto y) { return x.first > y.first; });

  rep(i, N) {
    if (i % 2 == 0) {
      // turn for A
      result += A[pairs[i].second];
      // cout << "turn A"
      //      << " index:" << pairs[i].second << " value" << A[pairs[i].second]
      //      << endl;
    } else {
      // turn for B
      result -= B[pairs[i].second];
      // cout << "turn B"
      //      << " index:" << pairs[i].second << " value" << B[pairs[i].second]
      //      << endl;
    }
    // cout << pairs[i].first << " " << pairs[i].second << endl;
  }
  cout << result << endl;

  return 0;
}
