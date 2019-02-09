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

vector<int> temp;

int solve(vector<int> x, int left, int right) {
  int mid, i, j, k;

  if (x.size() <= 1) return x[0];

  /* ここでは分割しているだけ */
  mid = (left + right) / 2;                /* 中央の値より */
  int result_l = solve(x, left, mid);      /* 左を再帰呼び出し */
  int result_r = solve(x, mid + 1, right); /* 右を再帰呼び出し */

  if (result_l <= result_r) {
    return result_l;
  } else {
    return result_r;
  }

  /* x[left] から x[mid] を作業領域にコピー */
  for (i = left; i <= mid; i++) temp[i] = x[i];

  /* x[mid + 1] から x[right] は逆順にコピー */
  for (i = mid + 1, j = right; i <= right; i++, j--) temp[i] = x[j];

  i = left;  /* i とj は作業領域のデーターを */
  j = right; /* k は配列の要素を指している */

  for (k = left; k <= right; k++) /* 小さい方から配列に戻す */
    if (temp[i] <= temp[j])       /* ここでソートされる */
      x[k] = temp[i++];
    else
      x[k] = temp[j--];
}

int main() {
  // result;
  int N = 0;

  int L;
  cin >> L;
  vector<int> A;
  // Aの値がOddなら1, Evenなら0
  vector<int> AOE;
  rep(i, L) {
    int a;
    cin >> a;
    A.push_back(a);
    AOE.push_back(a / 2);
  }

  N = count(AOE.begin(), AOE.end(), 0);
  if (A[0] == 0 && A[L - 1] == 0) N -= 1;

  cout << N << endl;
  return 0;
}
