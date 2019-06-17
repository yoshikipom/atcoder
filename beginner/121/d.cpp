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
  ll A, B;
  cin >> A >> B;

  if (A % 2 == 1) {
    ll temp = (B - A) % 4;
    ll result = A;
    for (ll i = B - temp + 1; i < B + 1; i++) {
      result = (result ^ i);
    }
    cout << result << endl;
  } else {
    ll temp = (B - A + 1) % 4;
    ll result = 0;
    for (ll i = B - temp + 1; i < B + 1; i++) {
      result = (result ^ i);
    }
    cout << result << endl;
  }

  return 0;
}
