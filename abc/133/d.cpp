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
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int N;
  cin >> N;
  vector<ll> A;
  rep(i, N) {
    int a;
    cin >> a;
    A.push_back(a * 2);
  }

  ll sum = 0;
  rep(i, N) {
    if (i % 2 == 0) {
      sum += A[i];
    } else {
      sum -= A[i];
    }
  }
  int X = sum / 2;
  cout << X;

  rep(i, N - 1) {
    cout << " ";
    X = A[i] - X;
    cout << X;
  }
  cout << endl;

  return 0;
}
