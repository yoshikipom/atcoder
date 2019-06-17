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

int main() {
  ll N, K;
  cin >> N >> K;

  vector<int> A;
  rep(i, N) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  ll result = 0;
  ll right = 0;
  ll sum = 0;
  for (int left = 0; left < N; left++) {
    while (right < N && sum < K) {
      sum += A[right];
      right++;
    }
    // cout << "sum" << sum << endl;

    if (right == left) {
      ++right;
    }
    if (sum >= K) {
      result += N - right + 1;
      sum -= A[left];
    }
  }

  cout << result << endl;

  return 0;
}
