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

  int count = 0;
  for (size_t i = 0; i < 4; i++) {
    if (N % 10 == 2) {
      count++;
    }
    N /= 10;
  }

  cout << count << endl;

  return 0;
}
