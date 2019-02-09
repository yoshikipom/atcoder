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
  int X;
  cin >> X;

  switch (X) {
    case 7:
    case 5:
    case 3:
      cout << "YES" << endl;
      break;

    default:
      cout << "NO" << endl;
      break;
  }
  return 0;
}
