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
  string A, B, C;
  cin >> N >> A >> B >> C;

  int count = 0;
  // N文字目についてチェック
  rep(i, N) {
    set<char> S;
    S.insert(A[i]);
    S.insert(B[i]);
    S.insert(C[i]);

    switch (S.size()) {
      case 1:
        break;
      case 2:
        count++;
        break;
      case 3:
        count += 2;
        break;
      default:
        cout << "error" << endl;
    }
  }

  cout << count << endl;
  return 0;
}
