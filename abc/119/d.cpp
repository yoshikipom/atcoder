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

// TODO:
// 最初に近いところにいっても、反対にもう１点があり、間に最初と同じ種類のがあると無駄
// 右の神社、左の神社、右の寺、左の寺に最初にいく4パターン*右or左の２パターンをチェックすればとけそう
ll solve(vector<ll> S, vector<ll> T, ll x) {
  ll result = 0;

  ll min_point = INF;
  ll min_point_d = INF;
  bool min_point_is_temple;

  rep(i, S.size()) {
    if (abs(S[i] - x) < min_point_d) {
      min_point = S[i];
      min_point_d = abs(S[i] - x);
      min_point_is_temple = false;
    }
  }

  rep(i, T.size()) {
    if (abs(T[i] - x) < min_point_d) {
      min_point = T[i];
      min_point_d = abs(T[i] - x);
      min_point_is_temple = true;
    }
  }

  int second_d = INF;
  if (min_point_is_temple) {
    rep(i, S.size()) {
      if (abs(S[i] - min_point) < second_d) {
        second_d = abs(S[i] - min_point);
      }
    }
  } else {
    rep(i, T.size()) {
      if (abs(T[i] - min_point) < second_d) {
        second_d = abs(T[i] - min_point);
      }
    }
  }

  result = min_point_d + second_d;

  return result;
}

int main() {
  int A, B, Q;
  cin >> A >> B >> Q;

  vector<ll> S;
  vector<ll> T;

  rep(i, A) {
    ll s;
    cin >> s;
    S.push_back(s);
  }

  rep(i, B) {
    ll t;
    cin >> t;
    T.push_back(t);
  }

  rep(i, Q) {
    ll x;
    cin >> x;

    ll result = solve(S, T, x);

    cout << result << endl;
  }

  return 0;
}
