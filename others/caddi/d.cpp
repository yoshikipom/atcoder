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
  vector<int> A;

  for (size_t i = 0; i < N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  string result = "second";
  for (int a : A) {
    if (a % 2 == 1) {
      result = "first";
    }
  }

  cout << result << endl;

  return 0;
}
