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
  ll N;
  cin >> N;
  vector<ll> A;
  rep(i, N) {
    ll a;
    cin >> a;
    A.push_back(a);
  }

  sort(A.begin(), A.end());

  vector<pair<ll, ll>> P;
  for (ll i = 1; i < N - 1; i++) {
    pair<ll, ll> p;
    if (A[i] >= 0) {
      p = make_pair(A[0], A[i]);
      A[0] -= A[i];
    } else {
      p = make_pair(A[N - 1], A[i]);
      A[N - 1] -= A[i];
    }
    P.push_back(p);
  }

  pair<ll, ll> p = make_pair(A[N - 1], A[0]);
  P.push_back(p);
  ll result = A[N - 1] - A[0];

  cout << result << endl;
  for (pair<ll, ll> p : P) {
    cout << p.first << " " << p.second << endl;
  }

  return 0;
}
