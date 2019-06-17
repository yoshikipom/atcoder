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

vector<vector<int>> vvi;

typedef struct _point {
  int x;
  int y;
  bool operator<(const _point& rhs) const {
    if (x < rhs.x) return true;
    if (x > rhs.x) return false;
    if (y < rhs.y) return true;
    if (y > rhs.y) return false;
    return false;
  }
  bool operator==(const _point& rhs) const {
    return (x == rhs.x && y == rhs.y);
  }
} Point;

// 成功したtrueを返す
bool combine_if_connect(vector<vector<Point>> turn2, int i, int j) {
  bool flag = false;
  vector<Point> v1 = turn2[i];
  vector<Point> v2 = turn2[j];
  rep(k, v1.size()) {
    rep(l, v2.size()) {
      if (v1[k] == v2[l]) {
        flag = true;
        goto RET;
      }
    }
  }
RET:
  return false;
}

int main() {
  int H, W;
  cin >> H >> W;
  vector<string> S;
  string s0 = "--";
  rep(i, W) { s0 += "-"; }
  S.push_back(s0);
  rep(i, H) {
    string s;
    cin >> s;
    S.push_back("-" + s + "-");
  }
  S.push_back(s0);

  // vvi = vector<vector<int>>(H, vector<int>(W, 0));\

  // turn0 黒の場所を見つける
  vector<Point> black_list;
  rep(i, H + 2) {
    rep(j, W + 2) {
      if (S[i][j] == '#') {
        Point black = {i, j};
        black_list.push_back(black);
      }
    }
  }

  // turn1 黒と白のペアを作る
  map<Point, set<Point>> turn1;
  for (auto it = black_list.begin(), end = black_list.end(); it != end; ++it) {
    Point black = *it;
    int x = black.x;
    int y = black.y;
    if (S[x - 1][y] == '.') {
      Point white = {x - 1, y};
      turn1[black].insert(white);
    }
    if (S[x + 1][y] == '.') {
      Point white = {x + 1, y};
      turn1[black].insert(white);
    }
    if (S[x][y - 1] == '.') {
      Point white = {x, y - 1};
      turn1[black].insert(white);
    }
    if (S[x][y + 1] == '.') {
      Point white = {x, y + 1};
      turn1[black].insert(white);
    }
  }

  // turn2 黒と黒のセットを作る
  bool flag = true;
  vector<vector<Point>> turn2;
  rep(i, black_list.size()) {
    vector<Point> ss;
    ss.push_back(black_list[i]);
    turn2.push_back(ss);
  }
  while (flag) {
    flag = false;
    rep(i, turn2.size()) {
      rep(j, i) { flag = combine_if_connect(turn2, i, j); }
    }
  }

  rep(i, H + 2) {
    rep(j, W + 2) { cout << S[i][j]; }
    cout << endl;
  }

  return 0;
}
