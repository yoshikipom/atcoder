#include <algorithm>
#include <cmath>
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
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
#define rep(i, n) for (int i = 0; i < n; i++)

template <typename Iterator>
std::vector<Iterator> divideInto(int n, Iterator begin, Iterator end) {
  std::vector<Iterator> result;
  const int length = std::distance(begin, end);
  const int partial_length = (length + n - 1) / n;

  for (Iterator i = begin; i < end; std::advance(i, partial_length)) {
    result.push_back(i);
  }
  result.push_back(end);

  return result;
}

void disp(vector<int> V) {
  for (int v : V) {
    cout << v << " ";
  }
  cout << endl;
}

vector<int> newVec(vector<int>::iterator begin, vector<int>::iterator end) {
  vector<int> result;
  auto it = begin;
  int temp = 0;
  while (it != end) {
    if (temp != *it) {
      result.push_back(*it);
      temp = *it;
    }
    it++;
  }
  return result;
}

int solve(vector<int> v) {
  cout << "solve" << endl;
  if (v.size() == 0) {
    return 1;
  }

  int result = 1;
  bool flag = true;
  for (size_t i = 0; i < v.size() - 1; i++) {
    for (size_t j = i + 1; j < v.size(); j++) {
      if (v[i] == v[j]) {
        disp(v);
        cout << "i:" << i << " j:" << j << endl;
        vector<int> next = newVec(v.begin() + i + 1, v.begin() + j - 1);
        result *= solve(next);
      }
    }
  }
  return result;
}

int main() {
  int N;
  cin >> N;
  vector<int> C;
  rep(i, N) {
    int c;
    cin >> c;
    C.push_back(c);
  }

  vector<int> newC = newVec(C.begin(), C.end());

  cout << solve(newC) << endl;

  return 0;
}
