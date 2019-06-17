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

bool checkDone(int H, int W, char A[H][W]) {
  rep(i, H) {
    rep(j, W) {
      if (A[i][j] == '.') {
        return true;
      }
    }
  }
  return false;
}

void solve(int H, int W, char A[H][W]) {
  rep(i, H) {
    rep(j, W) {
      if (checkDone(H, W, A) == true) {
      }
      cout << A[i][j];
    }
    cout << endl;
  }
  return;
}

int main() {
  int H, W;
  cin >> H >> W;
  char A[H][W];

  rep(i, H) {
    rep(j, W) { cin >> A[i][j]; }
  }

  solve(H, W, Ah);

  return 0;
}
