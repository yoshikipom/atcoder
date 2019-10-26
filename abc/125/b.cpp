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
  vector<int> V;
  vector<int> C;
  rep(i, N) {
    int v;
    cin >> v;
    V.push_back(v);
  }
  rep(i, N) {
    int c;
    cin >> c;
    C.push_back(c);
  }
  int result = 0;
  rep(i, N) {
    int point = V[i] - C[i];
    if (point > 0) {
      result += point;
    }
  }
  cout << result << endl;
  return 0;
}
