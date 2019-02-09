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

// できること
// Sの２種類の文字を入れ替える
// Sの１種類の文字を使われていない文字で交換する

// 組み合わせを作れて並べられたら完成
// 各種類の文字数確認

// 位置と数が合っているかチェックすればok?

// string solve(string s, char c1, char c2) {
//   rep(i, s.size()) {
//     if (s[i] == c1) {
//       s[i] = c2;
//     } else if (s[i] == c2) {
//       s[i] = c1;
//     }
//   }
//   cout << s << endl;
//   return s;
// }

int main() {
  // string s;
  // cin >> s;
  // while (true) {
  //   char c1, c2;
  //   cin >> c1 >> c2;
  //   s = solve(s, c1, c2);
  // }

  string S, T;
  cin >> S >> T;
  // 各文字がどのindexにあるか
  map<char, vector<int>> s_map, t_map;
  for (int i = 0; i < S.size(); i++) {
    s_map[S[i]].push_back(i);
  }
  for (int i = 0; i < T.size(); i++) {
    t_map[T[i]].push_back(i);
  }

  set<int> skip_index;
  bool is_ok = true;
  for (int i = 0; i < S.size(); i++) {
    if (!skip_index.count(i)) {
      if (!equal(s_map[S[i]].cbegin(), s_map[S[i]].cend(),
                 t_map[T[i]].cbegin())) {
        is_ok = false;
        break;
      } else {
        for (int index : s_map[S[i]]) skip_index.insert(index);
      }
    }
  }

  if (is_ok) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
