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
typedef long long unsigned int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

template <typename T>
void remove(std::vector<T>& vector, unsigned int index) {
  vector.erase(vector.begin() + index);
}

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> X;
  rep(i, M) {
    int x;
    cin >> x;
    X.push_back(x);
  }

  sort(X.begin(), X.end());

  vector<vector<int>> XX;
  XX.push_back(X);
  int answer = 0;

  rep(j, N - 1) {
    cout << "loop" << j << endl;
    int split_x_index;
    // 分ける対象を決定
    int split_x_num = INF;
    for (int i = 0; i < XX.size(); i++) {
      int div = *XX[i].end() - *XX[i].begin();
      if (split_x_num > div) {
        split_x_num = div;
        split_x_index = i;
        cout << "index " << i << endl;
      }
    }

    vector<int> Xi = XX[split_x_index];
    remove(XX, split_x_index);

    int result = INF;
    int result_index = 0;
    // iの後ろで分ける
    for (int i = 1; i < M - 1; i++) {
      int left = (Xi[i] - Xi[0]);
      int right = (Xi[M - 1] - Xi[i + 1]);
      int sum = left + right;
      if (sum < result) {
        // cout << "result " << sum << endl;
        result = sum;
        // cout << "index " << i << endl;
        result_index = i;
      }
    }

    vector<int> X1;
    vector<int> X2;
    for (int i = 0; i < result_index + 1; i++) {
      X1.push_back(Xi[i]);
    }
    for (int i = result_index + 1; i < Xi.size(); i++) {
      X2.push_back(Xi[i]);
    }
    XX.push_back(X1);
    XX.push_back(X2);
  }

  // output
  for (vector<int> X : XX) {
    for (int x : X) {
      cout << x << " ";
    }
    cout << endl;
  }

  return 0;
}
