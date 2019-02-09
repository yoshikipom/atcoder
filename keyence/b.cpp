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
  string S;
  cin >> S;

  bool flag = false;

  rep(i, S.size()) {
    rep(j, S.size() - i) {
      string temp(S);
      temp.erase(temp.begin() + i, temp.begin() + i + j);
      // cout << temp << endl;
      if (temp == "keyence") {
        cout << "YES" << endl;
        flag = true;
        break;
      }
    }
    if (flag == true) {
      break;
    }
  }

  if (!flag) cout << "NO" << endl;

  return 0;
}
