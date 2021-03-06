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
  int N, X;
  cin >> N >> X;
  vector<int> L;
  rep(i, N) {
    int l;
    cin >> l;
    L.push_back(l);
  }

  int D = 0;
  int result = 1;
  rep(i, N) {
    D += L[i];
    if (D > X) {
      break;
    } else {
      result++;
    }
  }
  cout << result << endl;

  return 0;
}
