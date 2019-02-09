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

const vector<ll> materials = {3, 5, 7};
vector<ll> nums753;

ll map_num(vector<int> indexes) {
  ll result = 0;
  for (int i = 0; i < indexes.size(); i++) {
    result += materials[indexes[i]] * powl(10, i);
  }
  return result;
}

// 753条件を満たすか
bool check_indexes(vector<int> indexes) {
  bool has3 = false;
  bool has5 = false;
  bool has7 = false;
  for (int index : indexes) {
    switch (index) {
      case 0:
        has3 = true;
        break;
      case 1:
        has5 = true;
        break;
      case 2:
        has7 = true;
        break;
    }
  }
  return has3 && has5 && has7;
}

void _make(vector<int> indexes, int cur) {
  while (true) {
    if (check_indexes(indexes)) {
      ll num = map_num(indexes);
      nums753.push_back(num);
    }
    indexes[cur]++;

    // 繰り上げ
    for (int i = 0; i < indexes.size(); i++) {
      if (indexes[i] > materials.size() - 1) {
        // 繰り上げ発生時の処理
        indexes[i] = 0;
        if (i + 1 > indexes.size() - 1) {
          return;
        }
        indexes[i + 1] += 1;
      } else {
        break;
      }
    }
  }
}

// N桁のときの753数を作る
void make(int N) {
  vector<int> indexes(N, 0);
  _make(indexes, 0);
}

int main() {
  ll N;
  cin >> N;

  for (int i = 3; i < 10; i++) {
    make(i);
  }

  ll count = 0;
  for (ll num : nums753) {
    if (num <= N) {
      count++;
    } else {
      break;
    }
  }
  cout << count << endl;

  // for (ll num : nums753) cout << num << endl;
  // cout << nums753.size() << endl;
  return 0;
}
