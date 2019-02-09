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
  int D;
  cin >> D;
  switch (D) {
    case 22:
      cout << "Christmas Eve Eve Eve" << endl;
      break;
    case 23:
      cout << "Christmas Eve Eve" << endl;
      break;
    case 24:
      cout << "Christmas Eve" << endl;
      break;
    case 25:
      cout << "Christmas" << endl;
      break;
  }
  return 0;
}
