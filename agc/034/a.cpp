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

string S;

// startからendまでに２個連続の岩がないときtrue
int check1(int start, int end) {
  for (int i = start; i < end; i++) {
    if (S[i] == '#' && S[i + 1] == '#') {
      return false;
    }
  }
  return true;
}

// startからendまでにBがAに乗り越えられることのできる点があればtrue
int check2(int start, int end) {
  for (int i = start; i <= end; i++) {
    if (S[i - 1] == '.' && S[i] == '.' && S[i + 1] == '.') {
      return true;
    }
  }
  return false;
}

int main() {
  int n, a, b, c, d;
  cin >> n >> a >> b >> c >> d;
  cin >> S;

  S = "#" + S;

  bool flag1 = true;
  bool flag2 = true;

  flag1 = check1(a, c) && check1(b, d);

  if (d < c) {
    flag2 = check2(b, d);
  }

  string result;

  if (flag1 && flag2) {
    result = "Yes";
  } else {
    result = "No";
  }

  cout << result << endl;

  return 0;
}
