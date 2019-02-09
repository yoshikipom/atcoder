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
  ll N, H, W;
  cin >> N >> H >> W;

  vector<ll> A;
  vector<ll> B;

  for (size_t i = 0; i < N; i++) {
    ll a, b;
    cin >> a >> b;
    A.push_back(a);
    B.push_back(b);
  }

  ll result = 0;
  for (int i = 0; i < N; i++) {
    if (A[i] >= H && B[i] >= W) {
      result++;
    }
  }

  cout << result << endl;

  return 0;
}
