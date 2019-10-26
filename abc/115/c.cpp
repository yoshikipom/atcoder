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

int main() {
  ll N, K;
  cin >> N;
  cin >> K;
  vector<ll> H;

  for (size_t i = 0; i < N; i++) {
    ll h;
    cin >> h;
    H.push_back(h);
  }

  sort(H.begin(), H.end());

  ll result = INF;
  for (size_t i = 0; i < N - K; i++) {
    ll height_diff = H[i] - H[(K - 1)];
    if (height_diff < result) {
      result = height_diff;
    }
  }

  cout << result << endl;

  return 0;
}
