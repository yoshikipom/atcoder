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

// vectorからindex番目の要素を削除する
template <typename T>
void remove(std::vector<T>& vector, unsigned int index) {
  vector.erase(vector.begin() + index);
}

int main() {
  int H, W;
  cin >> H >> W;
  vector<vector<char>> A;
  rep(i, H) {
    vector<char> Aa;
    rep(j, W) {
      char a;
      cin >> a;
      Aa.push_back(a);
    }
    A.push_back(Aa);
  }

  bool w_ng = true;
  bool h_ng = true;
  while (w_ng || h_ng) {
    w_ng = false;
    h_ng = false;
    rep(i, H) {
      set<char> S;
      rep(j, W) S.insert(A[i][j]);
      if (S.size() == 1 && S.count('.') == 1) {
        remove(A, i);
        H--;
        h_ng = true;
      }
    }

    rep(i, W) {
      set<char> S;
      rep(j, H) S.insert(A[j][i]);
      if (S.size() == 1 && S.count('.') == 1) {
        rep(j, H) remove(A[j], i);
        W--;
        w_ng = true;
      }
    }
  }

  rep(i, H) {
    rep(j, W) { cout << A[i][j]; }
    cout << endl;
  }

  return 0;
}
