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
  int a, b;
  cin >> a >> b;
  int c = a * b;
  if (c % 2 == 0) {
    cout << "Even" << endl;
  } else if (c % 2 == 1) {
    cout << "Odd" << endl;
  } else {
    cout << "error" << endl;
  }
  return 0;
}
