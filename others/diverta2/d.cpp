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
  ll N, ga, sa, ba, gb, sb, bb;
  cin >> N >> ga >> sa >> ba >> gb >> sb >> bb;

  pair<ll, ll> g_pair = make_pair(ga, gb);
  pair<ll, ll> s_pair = make_pair(ga, gb);
  pair<ll, ll> b_pair = make_pair(ga, gb);

  vector<pair<ll, ll>> P;
  P.push_back(g_pair);
  P.push_back(s_pair);
  P.push_back(b_pair);

  sort(P.begin(), P.end(), [](const pair<ll, ll> &a, const pair<ll, ll> &b) {
    return a.second / a.first < b.second / b.first;
  });

  // a-> b
  vector<ll> buy_a;
  for (pair<ll, ll> p : P) {
    if (p.second / p.first > 1) {
      ll buy = N / p.first;
      N -= buy * p.first;
      buy_a.push_back(buy);
    }
  }
  for (pair<ll, ll> p : P) {
    if (p.second / p.first > 1) {
    }
  }

  if (P[2].second / P[2].first < 1) {
    // nothing
  } else {
    ll buy1 = N / P[2].first;
    N -= buy1 * P[2].first;
    ll buy2 = N / P[1].first;
    N -= buy2 * P[1].first;
    ll buy3 = N / P[0].first;
    N -= buy3 * P[0].first;
    N += buy1 * P[2].second;
    N += buy2 * P[2].second;
    N += buy3 * P[2].second;
  }

  // cout << N << endl;

  // b->a
  // cout << R[0] << endl;
  if (P[0].second / P[0].first > 1) {
    // nothing
  } else {
    N = floor(N / R[0]);
  }

  cout << N << endl;
  return 0;
}
