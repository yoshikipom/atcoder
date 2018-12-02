#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int N, M, f[12][12] = {0}, ans = 0;
void dfs(vector<int> v, int k = 0) {
  if (k == N) {
    for (int i = 0; i < v.size(); i++) {
      for (int j = i + 1; j < v.size(); j++) {
        if (f[v[i]][v[j]] == 0) {
          return;
        }
      }
    }
    ans = max(ans, (int)v.size());
  } else {
    dfs(v, k + 1);
    v.push_back(k);
    dfs(v, k + 1);
    v.pop_back();
  }
}

int main(int argc, char const *argv[]) {
  std::cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int x, y;
    std::cin >> x >> y;
    x--;
    y--;
    f[x][y] = f[y][x] = 1;
  }

  vector<int> v;
  dfs(v);
  std::cout << ans << '\n';
  return 0;
}
