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

vector<char> T;
vector<char> D;
int N, Q;
string s;
int left_g = 0;
int right_g = 0;

void disp(vector<int> v) {
  for (int i : v) {
    cout << i << " ";
  }
  cout << endl;
}

bool check_l(int index) {
  rep(i, Q) {
    if (T[i] == s[index]) {
      if (D[i] == 'L') {
        if (index == 0) {
          return true;
        }
        index--;
      } else {
        if (index == s.size() - 1) {
          return false;
        }
        index++;
      }
    }
  }
  return false;
}

bool check_r(int index) {
  rep(i, Q) {
    if (T[i] == s[index]) {
      if (D[i] == 'L') {
        if (index == 0) {
          return false;
        }
        index--;
      } else {
        if (index == s.size() - 1) {
          return true;
        }
        index++;
      }
    }
  }
  return false;
}

void solve_l() {
  int low = 0;
  int high = s.size() - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (check_l(mid)) {
      if (mid == s.size() - 1 || !check_l(mid + 1)) {
        left_g = mid + 1;
        // cout << "mid " << mid << " left_g " << left_g << endl;
        break;
      }
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
}

void solve_r() {
  int low = 0;
  int high = s.size() - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    if (check_r(mid)) {
      if (mid == 0 || !check_r(mid - 1)) {
        right_g = s.size() - (mid);
        // cout << "mid " << mid << " right_g " << right_g << endl;
        break;
      }
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
}

// Qlog(N)にしたい
int main() {
  cin >> N >> Q;

  cin >> s;

  rep(i, Q) {
    char t, d;
    cin >> t >> d;
    T.push_back(t);
    D.push_back(d);
  }

  solve_l();
  solve_r();

  // cout << "left_g " << left_g << endl;
  // cout << "right_g " << right_g << endl;

  int result = N - left_g - right_g;

  cout << result << endl;

  return 0;
}
