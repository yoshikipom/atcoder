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
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

void printV(vector<ll> V) {
  for (ll i : V) {
    cout << i << " ";
  }
  cout << endl;
}

int main() {
  int N;
  cin >> N;
  vector<ll> A;
  vector<ll> B;
  rep(i, N) {
    ll a;
    cin >> a;
    A.push_back(a);
  }
  rep(i, N) {
    ll b;
    cin >> b;
    B.push_back(b);
  }

  if (accumulate(A.begin(), A.end(), 0) < accumulate(B.begin(), B.end(), 0)) {
    cout << -1 << endl;
    return 0;
  }

  // 差をとる
  vector<ll> D;
  rep(i, N) {
    ll d = A[i] - B[i];
    D.push_back(d);
  }
  sort(D.begin(), D.end());
  // cout << "sorted" << endl;
  // printV(D);

  ll count = 0;
  ll temp = 0;
  int i = 0;
  while (true) {
    //終了条件
    if (D[i] >= 0) {
      break;
    }

    // 大きいほうの値をかりる
    if (temp <= 0) {
      for (int j = N - 1; j >= 0; j--) {
        if (D[j] > 0) {
          temp = D[j];
          D[j] = 0;
          count++;
          // cout << "big temp" << temp << endl;
          // printV(D);
          break;
        }
        if (D[j] < 0) {
          cout << count << endl;
          return 0;
        }
      }
    }

    // cout << "before: temp " << temp << " count " << count << endl;
    // printV(D);
    // 小さいやつに分け与える
    if (-D[i] > temp) {
      D[i] += temp;
      temp = 0;
    } else if (-D[i] <= temp) {
      temp += D[i];
      D[i] = 0;
      count++;
      i++;
    }
    // cout << "after: temp " << temp << " count " << count << endl;
    // printV(D);
    // cout << endl;
  }

  cout << count << endl;

  return 0;
}
