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
  vector<vector<int>> V;
  vector<int> v1;
  vector<int> v2;
  vector<int> v3;
  vector<int> v4;
  V.push_back(v1);
  V.push_back(v2);
  V.push_back(v3);
  V.push_back(v4);

  rep(i, 3) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    V[a].push_back(b);
    V[b].push_back(a);
  }

  for (vector<int> v : V) {
    if (v.size() >= 3) {
      cout << "NO" << endl;
      return 0;
    }
  }
  cout << "YES" << endl;
  return 0;
}
