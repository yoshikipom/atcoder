#include <algorithm>
#include <array>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
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
typedef long long ll;

// #define EPS (1e-7)
// #define INF (1e9)
// #define PI (acos(-1))

// array<ll, 100000> P;
// array<ll, 100000> Y;

// int main() {
//   ll N, M;
//   cin >> N >> M;
//   // vector<int> P, Y;
//   for (ll i = 0; i < M; i++) {
//     ll p, y;
//     // cin >> p >> y;
//     // scanf("%d %d", &p, &y);
//     // P.push_back(p);
//     // Y.push_back(y);
//     scanf("%d %llx", &P[i], &Y[i]);
//   }

//   map<ll, vector<ll>> m;
//   for (ll i = 0; i < M; i++) {
//     m[P[i]].push_back(Y[i]);
//   }

//   for (map<ll, vector<ll>>::iterator it = m.begin(), end = m.end(); it !=
//   end;
//        ++it) {
//     sort(it->second.begin(), it->second.end());
//   }

//   for (ll i = 0; i < M; i++) {
//     vector<ll> v = m[P[i]];
//     vector<ll>::iterator itr;
//     itr = lower_bound(v.begin(), v.end(), Y[i]);
//     // cout << setfill('0') << setw(6) << right << P[i];
//     // cout << setfill('0') << setw(6) << right << itr - v.begin() + 1;
//     // cout << endl;
//     printf("%012lld\n", ll(P[i]) * 1000000 + ll(itr - v.begin() + 1));
//   }
//   return 0;
// }

#define rep(i, n) for (int i = 0; i < n; i++)
int N, M;
int P[100000], Y[100000];
vector<int> yd[100001];

int main() {
  scanf("%d%d", &N, &M);
  rep(i, M) scanf("%d%d", &P[i], &Y[i]), yd[P[i]].push_back(Y[i]);
  rep(i, N) sort(yd[i + 1].begin(), yd[i + 1].end());
  rep(i, M) printf("%012lld\n",
                   ll(P[i]) * 1000000 +
                       int(lower_bound(yd[P[i]].begin(), yd[P[i]].end(), Y[i]) -
                           yd[P[i]].begin()) +
                       1);
  return 0;
}
