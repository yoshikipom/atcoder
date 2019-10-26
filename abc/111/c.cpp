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

int main() {
  int n;
  cin >> n;
  vector<int> V1, V2;
  rep(i, n / 2) {
    int v1, v2;
    cin >> v1 >> v2;
    V1.push_back(v1);
    V2.push_back(v2);
  }

  int count = 0;

  map<int, int> M1;
  for (int num : V1) {
    if (M1.count(num) == 0) {
      M1[num] = 1;
    } else {
      M1[num]++;
    }
  }

  map<int, int> M2;
  for (int num : V2) {
    if (M2.count(num) == 0) {
      M2[num] = 1;
    } else {
      M2[num]++;
    }
  }

  int max_key_11 = 0;
  int max_value_11 = 0;
  for (auto it = M1.begin(), end = M1.end(); it != end; ++it) {
    if (max_value_11 < it->second) {
      max_key_11 = it->first;
      max_value_11 = it->second;
    }
  }
  M1.erase(max_key_11);

  int max_key_12 = 0;
  int max_value_12 = 0;
  for (auto it = M1.begin(), end = M1.end(); it != end; ++it) {
    if (max_value_12 < it->second) {
      max_key_12 = it->first;
      max_value_12 = it->second;
    }
  }

  int max_key_21 = 0;
  int max_value_21 = 0;
  for (auto it = M2.begin(), end = M2.end(); it != end; ++it) {
    if (max_value_21 < it->second) {
      max_key_21 = it->first;
      max_value_21 = it->second;
    }
  }
  M2.erase(max_key_21);

  int max_key_22 = 0;
  int max_value_22 = 0;
  for (auto it = M2.begin(), end = M2.end(); it != end; ++it) {
    if (max_value_22 < it->second) {
      max_key_22 = it->first;
      max_value_22 = it->second;
    }
  }

  // cout << max_key_11 << endl;
  // cout << max_key_12 << endl;
  // cout << max_key_21 << endl;
  // cout << max_key_22 << endl;

  int result = 0;
  if (max_key_11 == max_key_21) {
    if (max_value_11 + max_value_22 > max_value_21 + max_value_12) {
      max_value_21 = max_value_22;
    } else {
      max_value_11 = max_value_12;
    }
  }
  result += V1.size() - max_value_11;
  result += V2.size() - max_value_21;

  cout << result << endl;

  return 0;
}
