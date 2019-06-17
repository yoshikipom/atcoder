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
  int A, B;
  cin >> A >> B;

  int result = 0;
  if (A > B) {
    result += A;
    A--;
  } else {
    result += B;
    B--;
  }
  if (A > B) {
    result += A;
    A--;
  } else {
    result += B;
    B--;
  }

  cout << result << endl;

  return 0;
}
