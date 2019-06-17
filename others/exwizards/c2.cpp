#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
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

void disp(vector<int> v) {
  for (int i : v) {
    cout << i << " ";
  }
  cout << endl;
}

int main() {
  int N, Q;
  cin >> N >> Q;

  string s;
  cin >> s;

  vector<char> T;
  vector<char> D;
  rep(i, Q) {
    char t, d;
    cin >> t >> d;
    T.push_back(t);
    D.push_back(d);
  }

  vector<int> G(N, 1);
  vector<int> check(N, 0);
  int god1 = 0;
  int god2 = N - 1;

  for (int i = Q - 1; i >= 0; i--) {
    char t = T[i];
    char d = D[i];
    if (t == s[god1]) {
      if (d == 'R' && god1 < N - 1) {
        god1++;
        check[god1] = 1;
      } else if (d == 'L' && god1 > 0) {
        god1--;
        check[god1] = 1;
      } else {
        cout << "error" << endl;
      }
    }
    if (t == s[god2]) {
      if (d == 'R' && god2 < N - 1) {
        god2++;
        check[god2] = 1;
      } else if (d == 'L' && god2 > 0) {
        god2--;
        check[god2] = 1;
      }
    }
  }

  int result = accumulate(check.begin(), check.end(), 0);
  disp(check);

  cout << result << endl;

  return 0;
}
