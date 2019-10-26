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
  vector<int> v = {1, 2, 3, 4, 5, 6};

  int N;
  cin >> N;

  for (size_t i = 0; i < N; i++) {
    int temp;
    temp = v[i % 5 + 1];
    v[i % 5 + 1] = v[i % 5];
    v[i % 5] = temp;
  }

  for (size_t i = 0; i < 6; i++) {
    cout << v[i];
  }

  return 0;
}
