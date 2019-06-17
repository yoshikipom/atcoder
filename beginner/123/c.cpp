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
  ll N;
  cin >> N;
  vector<ll> V;
  rep(i, 5) {
    ll v;
    cin >> v;
    V.push_back(v);
  }

  sort(V.begin(), V.end());

  ll target = V[0];

  ll additional = ceil(1.0 * N / target) - 1;

  ll result = 5 + additional;

  cout << result << endl;
  return 0;
}
