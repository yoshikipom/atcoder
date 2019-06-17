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
  vector<int> times;
  rep(i, 5) {
    int time;
    cin >> time;
    times.push_back(time);
  }

  int lastIndex;
  int lastTimeDev = 10;
  rep(i, 5) {
    if (times[i] % 10 != 0) {
      if (times[i] % 10 < lastTimeDev) {
        lastIndex = i;
        lastTimeDev = times[i] % 10;
      }
    }
  }

  int result = 0;
  rep(i, 5) {
    if (i != lastIndex) {
      result += ceil(1.0 * times[i] / 10) * 10;
      // cout << result << endl;
    }
  }
  result += times[lastIndex];
  cout << result << endl;

  return 0;
}
