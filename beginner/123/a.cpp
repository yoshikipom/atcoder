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
  vector<int> v;
  rep(i, 5) {
    int a;
    cin >> a;
    v.push_back(a);
  }

  int k;
  cin >> k;

  bool result = true;
  rep(i, 5) {
    rep(j, 5) if (abs(v[i] - v[j]) > k) { result = false; }
  }

  if (result) {
    cout << "Yay!" << endl;
  } else {
    cout << ":(" << endl;
  }

  return 0;
}
