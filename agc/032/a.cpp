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

void disp(vector<int> V) {
  for (int i : V) {
    cout << i << " ";
  }
  cout << endl;
}

int main() {
  int N;
  cin >> N;
  vector<int> B;
  rep(i, N) {
    int b;
    cin >> b;
    B.push_back(b);
  }

  stack<int> S;

  bool isSuccess = true;
  int M = B.size();
  rep(i, N) {
    bool hasPop = false;
    for (int k = M - 1; k >= 0; k--) {
      // cout << "i, k =" << i << " " << k << endl;
      if (B[k] == k + 1) {
        B.erase(B.begin() + k);
        M--;
        S.push(k + 1);
        hasPop = true;
        // cout << "break" << endl;
        break;
      }
    }
    if (!hasPop) {
      isSuccess = false;
      break;
    }
  }

  // cout << "result" << endl;

  if (isSuccess) {
    rep(i, N) {
      cout << S.top() << endl;
      S.pop();
    }
  } else {
    cout << -1 << endl;
  }

  return 0;
}
