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
  // A, C, G, T が存在し、A と T、C と
  char b;
  cin >> b;

  char ans;
  if (b == 'A') {
    ans = 'T';
  } else if (b == 'C') {
    ans = 'G';
  } else if (b == 'G') {
    ans = 'C';
  } else if (b == 'T') {
    ans = 'A';
  }

  cout << ans << endl;

  return 0;
}
