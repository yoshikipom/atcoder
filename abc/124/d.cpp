#include <stdio.h>
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

class Point {
 public:
  int left;
  int right;
};

template <typename T>
void remove(std::vector<T>& vector, unsigned int index) {
  vector.erase(vector.begin() + index);
}

int dryPush(string src, Point* p) {
  string s(src);
  for (int i = p->left; i <= p->right; i++) {
    s[i] = '1';
  }

  int max = 0;
  int count = 0;
  rep(i, s.size()) {
    if (s[i] == '1') {
      count++;
    } else {
      if (count > max) {
        max = count;
      }
      count = 0;
    }
  }
  if (count > max) {
    max = count;
  }

  return max;
}

int main() {
  int N, K;
  cin >> N >> K;
  string S;
  cin >> S;

  bool down = false;
  int left;
  int right;
  vector<Point*> P;
  rep(i, N) {
    if (down) {
      if (S[i] == '1') {
        right = i - 1;
        Point* p = new Point();
        p->left = left;
        p->right = right;
        P.push_back(p);
        down = false;
      }
    }
    if (S[i] == '0') {
      left = i;
      down = true;
    }
  }

  rep(i, K) {
    cout << "-----------" << i << "--------" << endl;
    int max = 0;
    int maxIndex = 0;
    rep(i, P.size()) {
      int temp = dryPush(S, P[i]);
      cout << P[i]->left << " " << P[i]->right << endl;
      cout << temp << endl;
      if (max < temp) {
        max = temp;
        maxIndex = i;
      }
    }

    for (int i = P[maxIndex]->left; i <= P[maxIndex]->right; i++) {
      S[i] = '1';
    }
    // cout << maxIndex << endl;

    remove(P, maxIndex);
  }

  int max = 0;
  int count = 0;
  rep(i, S.size()) {
    if (S[i] == '1') {
      count++;
    } else {
      if (count > max) {
        max = count;
      }
      count = 0;
    }
  }
  if (count > max) {
    max = count;
  }
  cout << S << endl;
  cout << max << endl;

  return 0;
}
