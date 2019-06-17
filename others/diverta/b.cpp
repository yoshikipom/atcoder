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
  int R, G, B, N;
  cin >> R >> G >> B >> N;
  int count = 0;
  int r_max = N / R;
  int g_max = N / G;
  for (int i = 0; i <= r_max; i++) {
    for (int j = 0; j <= g_max; j++) {
      if (N - i * R - j * G < 0) {
        break;
      }
      bool flag = (N - i * R - j * G) % B == 0;
      if (flag) {
        count++;
      }
    }
  }

  cout << count << endl;

  return 0;
}
