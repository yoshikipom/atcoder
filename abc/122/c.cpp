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

// int getNumOfAc(string s) {
//   int count = 0;
//   bool prevIsA = false;
//   for (char c : s) {
//     if (c == 'C' && prevIsA) {
//       count++;
//     }

//     if (c == 'A') {
//       prevIsA = true;
//     } else {
//       prevIsA = false;
//     }
//   }
//   return count;
// }

int main() {
  int N, Q;
  cin >> N >> Q;

  string S;
  cin >> S;

  int DP1[N];
  int DP2[N];

  rep(i, N) { DP1[i] = 0; }
  rep(i, N) { DP2[i] = 0; }

  for (int i = 1; i < N; i++) {
    DP1[i] = DP1[i - 1];
    if (S[i - 1] == 'A' && S[i] == 'C') {
      DP1[i]++;
    }
    DP2[N - 1 - i] = DP2[N - 1 - i + 1];
    if (S[N - 1 - i] == 'A' && S[N - 1 - i + 1] == 'C') {
      DP2[N - 1 - i]++;
    }
    // cout << "i " << i << ", j " << j << ", DP" << DP[i][j] << endl;
  }

  vector<int> L;
  vector<int> R;
  rep(i, Q) {
    int l, r;
    cin >> l >> r;
    L.push_back(l);
    R.push_back(r);
    // string sub = S.substr(l - 1, r - l + 1);
    // cout << "sub: " << sub << endl;
  }

  rep(i, Q) {
    // cout << "ALL: " << DP2[0] << endl;
    // cout << "pre: " << DP1[L[i] - 1] << endl;
    // cout << "next: " << DP2[R[i] - 1] << endl;
    cout << DP1[N - 1] - DP1[L[i] - 1] - DP2[R[i] - 1] << endl;
  }

  // cout << DP[0][0] << endl;
  return 0;
}
