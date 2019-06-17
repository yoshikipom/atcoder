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
  float root = sqrt(N);
  ll result = 0;
  for (ll i = 1; i < root; i++) {
    // if (N / i == N % i) {
    // cout << "i: " << i << ", ";
    // cout << "div: " << N / i << ", " << N % i;
    // cout << endl;
    if ((N - i) % i == 0) {
      // cout << (N - i) / i << endl;
      result += (N - i) / i;
    }
    // }
  }

  cout << result << endl;

  return 0;
}
