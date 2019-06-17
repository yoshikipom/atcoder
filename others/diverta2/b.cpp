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
  cin >> N;
  vector<pair<ll, ll>> P;
  rep(i, N) {
    ll x, y;
    cin >> x >> y;
    pair<ll, ll> p = make_pair(x, y);
    P.push_back(p);
  }

  map<pair<ll, ll>, int> M;

  for (int i = 0; i < N - 1; i++) {
    for (int j = i + 1; j < N; j++) {
      pair<ll, ll> pi = P[i];
      pair<ll, ll> pj = P[j];
      bool reverse = false;
      if (pi.first > pj.first) {
        reverse = true;
      } else {
        if (pi.first == pj.first && pi.second > pj.second) {
          reverse = true;
        }
      }

      ll x;
      ll y;
      if (reverse) {
        x = pj.first - pi.first;
        y = pj.second - pi.second;
      } else {
        x = pi.first - pj.first;
        y = pi.second - pj.second;
      }

      pair<ll, ll> p_diff = make_pair(x, y);

      if (M.find(p_diff) != M.end()) {
        M[p_diff]++;
      } else {
        M[p_diff] = 1;
      }
    }
  }

  int no_cost = 0;
  for (auto it = M.begin(), end = M.end(); it != end; ++it) {
    // cout << it->first.first << " " << it->first.second << " " << it->second
    //  << endl;
    no_cost = max(no_cost, it->second);
  }

  cout << N - no_cost << endl;

  return 0;
}
