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
  int N, M, C;
  cin >> N >> M >> C;
  vector<int> B;
  rep(i, M) {
    int b;
    cin >> b;
    B.push_back(b);
  }

  int result = 0;
  rep(i, N) {
    vector<int> A;
    rep(i, M) {
      int a;
      cin >> a;
      A.push_back(a);
    }
    int temp = 0;
    rep(i, M) { temp += A[i] * B[i]; }
    temp += C;
    if (temp > 0) {
      result++;
    }
  }

  cout << result << endl;

  return 0;
}
