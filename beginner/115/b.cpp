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

int main() {
  int N;
  cin >> N;
  vector<int> P;

  for (size_t i = 0; i < N; i++) {
    int p;
    cin >> p;
    P.push_back(p);
  }

  sort(P.rbegin(), P.rend());

  int sum;
  for (size_t i = 0; i < N; i++) {
    if (i == 0) {
      sum += P[i] / 2;
    } else {
      sum += P[i];
    }
  }

  cout << sum << endl;

  return 0;
}
