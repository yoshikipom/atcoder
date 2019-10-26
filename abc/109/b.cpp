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
  vector<string> V;
  set<string> S;
  rep(i, N) {
    string s;
    cin >> s;
    V.push_back(s);
    if (S.count(V[i]) != 0) {
      cout << "No" << endl;
      return 0;
    }
    S.insert(s);
  }

  rep(i, N) {
    if (i != 0 && V[i - 1][V[i - 1].size() - 1] != V[i][0]) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
  return 0;
}
