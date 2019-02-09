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
  int n1, n2, n3, n4;
  bool flag1 = false;
  bool flag9 = false;
  bool flag7 = false;
  bool flag4 = false;

  vector<int> N;
  cin >> n1;
  cin >> n2;
  cin >> n3;
  cin >> n4;
  N.push_back(n1);
  N.push_back(n2);
  N.push_back(n3);
  N.push_back(n4);

  for (int n : N) {
    if (n == 1) {
      flag1 = true;
    }
    if (n == 9) {
      flag9 = true;
    }
    if (n == 7) {
      flag7 = true;
    }
    if (n == 4) {
      flag4 = true;
    }
  }

  if (flag1 && flag9 && flag7 && flag4) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}
