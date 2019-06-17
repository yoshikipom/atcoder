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

void disp(vector<int> v) {
  for (int i : v) {
    cout << i << " ";
  }
  cout << endl;
}

// Qlog(N)にしたい
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
  vector<int> G_temp(N, 1);
  int result = N;
  string s2 = "";

  rep(i, Q) {
    char t = T[i];
    char d = D[i];

    if (d == 'L') {
      s2 = t + s2;
    } else if (d == 'R') {
      s2 = s2 + t;
    }
  }

  cout << s2 << endl;

  // cout << "query: " << i + 1 << endl;
  // cout << "dict: " << endl;
  // disp(dict[t]);
  // cout << "result: " << result << endl;
  // disp(G);

  cout << result << endl;

  return 0;
}
