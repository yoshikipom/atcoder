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

map<int64_t, int> prime_factor(int64_t n) {
  map<int64_t, int> ret;
  for (int64_t i = 2; i * i <= n; i++) {
    while (n % i == 0) {
      ret[i]++;
      n /= i;
    }
  }
  if (n != 1) ret[n] = 1;
  return ret;
}

int main() {
  ll N, P;
  cin >> N >> P;

  ll result = 1;
  for (auto p : prime_factor(P)) {
    // cout << p.first << " " << p.second << endl;
    result *= pow(p.first, floor(p.second / N));
    // cout << result << endl;
  }

  cout << result << endl;

  return 0;
}
