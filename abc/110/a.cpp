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
  vector<int> V;
  int N = 3;
  rep(i, N) {
    int v;
    cin >> v;
    V.push_back(v);
  }
  sort(V.begin(), V.end());
  cout << 10 * V[2] + V[1] + V[0] << endl;

  return 0;
}
