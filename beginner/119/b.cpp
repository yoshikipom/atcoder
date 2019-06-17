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

int BTC_RATE = 380000;

int main() {
  float result = 0;

  int N;
  cin >> N;
  rep(i, N) {
    float x;
    string u;
    cin >> x >> u;
    if (u == "JPY") {
      result += x;
    } else if (u == "BTC") {
      result += x * BTC_RATE;
    } else {
      cout << "error" << endl;
    }
  }

  cout << result << endl;

  return 0;
}
