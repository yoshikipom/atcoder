

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

  ll temp = A;
  for (ll cur = A + 1; cur < B + 1; cur++) {
    temp = (temp ^ cur);
    cout << cur << " " << temp << endl;
  }

  cout << temp << endl;

  return 0;
}
