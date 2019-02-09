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
  vector<int> A;
  rep(i, N) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  int count = 0;
  int end_flag = false;
  do {
    for (int a : A) {
      if (a % 2 == 0) {
        a = a / 2;
        continue;
      } else {
        end_flag = true;
        break;
      }
    }
  } while (end_flag);
  count++;

  cout << count << endl;
  return 0;
}
