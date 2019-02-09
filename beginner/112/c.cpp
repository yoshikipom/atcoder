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
  int N;
  cin >> N;
  vector<int> X, Y, H;
  rep(i, N) {
    int x, y, h;

    cin >> x >> y >> h;
    X.push_back(x);
    Y.push_back(y);
    H.push_back(h);
  }

  bool end_flag = false;
  int result_x, result_y, result_h;
  rep(i, 101) {
    if (end_flag) break;
    rep(j, 101) {
      if (end_flag) break;
      end_flag = true;
      // resultを計算
      rep(k, N) {
        if (H[k] == 0) continue;
        result_x = i;
        result_y = j;
        result_h = H[k] + abs(X[k] - result_x) + abs(Y[k] - result_y);
        break;
      }

      //すべての調査結果に適合するか
      rep(k, N) {
        if (max(result_h - abs(X[k] - result_x) - abs(Y[k] - result_y), 0) ==
            H[k]) {
          continue;
        } else {
          end_flag = false;
          break;
        }
      }
    }
  }

  cout << result_x << " " << result_y << " " << result_h << endl;
  return 0;
}
