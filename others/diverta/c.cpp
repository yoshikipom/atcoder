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

std::vector<int> find_all(const std::string str, const std::string subStr) {
  std::vector<int> result;

  int subStrSize = subStr.size();
  int pos = str.find(subStr);

  while (pos != std::string::npos) {
    result.push_back(pos);
    pos = str.find(subStr, pos + subStrSize);
  }

  return result;
}

int main() {
  int N;
  cin >> N;
  vector<string> s_list;
  vector<int> end_a_list;
  vector<int> start_b_list;
  vector<int> both_list;
  int count = 0;
  rep(i, N) {
    string s;
    cin >> s;
    count += find_all(s, "AB").size();
    s_list.push_back(s);
    bool start_b = s[0] == 'B';
    bool end_a = s[s.size() - 1] == 'A';
    if (start_b && end_a) {
      both_list.push_back(i);
    } else if (start_b) {
      start_b_list.push_back(i);
    } else if (end_a) {
      end_a_list.push_back(i);
    }
  }

  if (both_list.size() == 0) {
    count += min(end_a_list.size(), start_b_list.size());
  } else {
    if (end_a_list.size() + start_b_list.size() == 0) {
      count += both_list.size() - 1;
    } else {
      count += both_list.size() + min(end_a_list.size(), start_b_list.size());
    }
  }
  cout << count << endl;

  return 0;
}
