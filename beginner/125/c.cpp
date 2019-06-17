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

unsigned gcd(unsigned a, unsigned b) {
  if (a == 0) {
    return b;
  } else if (b == 0) {
    return a;
  }
  if (a < b) gcd(b, a);
  unsigned r;
  while ((r = a % b)) {
    a = b;
    b = r;
  }
  return b;
}

void disp(vector<int> v) {
  rep(i, v.size()) { cout << v[i] << " "; }
  cout << endl;
}

int search_unused(vector<int> A) {
  int left = 0;
  int right = A.size() - 1;
  int left_gcd = A[left];
  int right_gcd = A[(right - left) / 2 + 1];

  while (left != right) {
    int mid = (right - left) / 2;
    for (int i = left; i <= mid; i++) {
      // cout << "temp1" << left_gcd << endl;
      left_gcd = gcd(left_gcd, A[i]);
      // cout << "temp2" << left_gcd << endl;
    }

    for (int i = mid + 1; i <= right; i++) {
      right_gcd = gcd(right_gcd, A[i]);
    }

    // cout << "left_g:" << left_gcd << ", right_g:" << right_gcd << endl;

    if (left_gcd > right_gcd) {
      left = mid + 1;
      right_gcd = left_gcd;
    } else {
      right = mid;
      left_gcd = right_gcd;
    }

    // cout << "left:" << left << ", right:" << right << endl;
  }

  return left;
}

int main() {
  int N;
  cin >> N;
  vector<int> A;
  rep(i, N) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  vector<int> L(N);
  vector<int> R(N);

  rep(i, N) {
    if (i == 0) {
      L[i] = A[0];
    } else {
      L[i] = gcd(L[i - 1], A[i]);
    }
  }

  for (int i = N - 1; i >= 0; i--) {
    if (i == N - 1) {
      R[i] = A[N - 1];
    } else {
      R[i] = gcd(R[i + 1], A[i]);
    }
  }

  // disp(L);
  // disp(R);

  int result = 0;
  rep(i, N) {
    int l = i == 0 ? 0 : L[i - 1];
    int r = i == N - 1 ? 0 : R[i + 1];
    int tmp = gcd(l, r);
    result = max(result, tmp);
  }

  cout << result << endl;

  return 0;
}
