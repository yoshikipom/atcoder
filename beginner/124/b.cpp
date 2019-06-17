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
  cin >> N;

  vector<int> M;
  rep(i, N) {
    int m;
    cin >> m;
    M.push_back(m);
  }

  int result = 0;
  int highest = 0;
  rep(i, N) {
    if (M[i] >= highest) {
      result++;
      highest = M[i];
    }
  }

  cout << result << endl;

  return 0;
}
