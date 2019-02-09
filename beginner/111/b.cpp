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
  int N;
  cin >> N;

  int result;
  while (N < 1000) {
    string str_N = to_string(N);
    set<char> S;
    for (char c : str_N) {
      S.insert(c);
    }
    if (S.size() == 1) {
      result = N;
      break;
    }
    N++;
  }
  cout << result << endl;
  return 0;
}
