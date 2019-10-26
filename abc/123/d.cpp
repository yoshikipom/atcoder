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
#define INF (1e11)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int x, y, z, k;
  cin >> x >> y >> z >> k;

  vector<ll> A;
  vector<ll> B;
  vector<ll> C;

  rep(i, x) {
    int a;
    cin >> a;
    A.push_back(a);
  }
  rep(i, y) {
    int b;
    cin >> b;
    B.push_back(b);
  }
  rep(i, z) {
    int c;
    cin >> c;
    C.push_back(c);
  }

  sort(A.rbegin(), A.rend());
  sort(B.rbegin(), B.rend());
  sort(C.rbegin(), C.rend());

  vector<int> result;

  int ai = 0;
  int bi = 0;
  int ci = 0;
  ll max = A[ai] + B[bi] + C[ci];
  result.push_back(max);
  ll diffa;
  ll diffb;
  ll diffc;
  while (result.size() < k) {
    if (ai >= x - 1) {
      diffa = INF;
    } else {
      diffa = A[ai] - A[ai + 1];
    }
    if (bi >= y - 1) {
      diffb = INF;
    } else {
      diffb = B[bi] - B[bi + 1];
    }
    if (ci >= z - 1) {
      diffc = INF;
    } else {
      diffc = C[ci] - C[ci + 1];
    }

    char goIndex;
    if (diffa <= diffb && diffa <= diffc) {
      cout << "debuga" << endl;
      result.push_back(A[ai + 1] + B[bi] + C[ci]);
      goIndex = 'a';
    }
    if (diffb <= diffc && diffb <= diffa) {
      result.push_back(A[ai] + B[bi + 1] + C[ci]);
      cout << "debugb" << endl;
      goIndex = 'b';
    }
    if (diffc <= diffa && diffc <= diffb) {
      result.push_back(A[ai] + B[bi] + C[ci + 1]);
      cout << "debugc" << endl;
      goIndex = 'c';
    }

    if (goIndex == 'a') ai++;
    if (goIndex == 'b') bi++;
    if (goIndex == 'c') ci++;
  }

  for (int num : result) {
    cout << num << endl;
  }

  return 0;
}
