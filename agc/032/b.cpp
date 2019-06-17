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

class Result {
 public:
  int i;
  int j;
};

int main() {
  int N;
  cin >> N;
  bool A[N - 1][N - 1];
  vector<Result *> resultSet;

  rep(i, N) {
    rep(j, N) { A[i][j] = false; }
  }

  if (N % 2 == 1) {
    rep(i, N / 2) { A[i][N - i - 2] = true; }
  } else {
    rep(i, N / 2) { A[i][N - i - 1] = true; }
  }

  rep(i, N) {
    for (int j = i + 1; j < N; j++) {
      if (!A[i][j]) {
        Result *result = new Result;
        result->i = i;
        result->j = j;
        resultSet.push_back(result);
      }
    }
  }

  cout << resultSet.size() << endl;
  for (Result *result : resultSet) {
    cout << result->i + 1 << " " << result->j + 1 << endl;
  }
  return 0;
}
