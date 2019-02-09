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
  int N, A, B;
  cin >> N >> A >> B;
  vector<int> P1;
  vector<int> P2;
  vector<int> P3;
  rep(i, N) {
    int p;
    cin >> p;
    if (p <= A) {
      P1.push_back(p);
    } else if (A < p && p <= B) {
      P2.push_back(p);
    } else if (B < p) {
      P3.push_back(p);
    }
  }

  int count = INF;
  count = min(count, (int)P1.size());
  count = min(count, (int)P2.size());
  count = min(count, (int)P3.size());

  cout << count << endl;

  return 0;
}
