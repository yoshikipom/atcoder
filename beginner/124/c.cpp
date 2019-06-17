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

int count(vector<char> v, char target) {
  int count = 0;
  for (char c : v) {
    if (c == target) {
      count++;
    }
  }
  return count;
}

int main() {
  string S;
  cin >> S;

  vector<char> even;
  vector<char> odd;
  for (int i = 0; i < S.size(); i++) {
    if (i % 2 == 0) {
      even.push_back(S[i]);
    } else {
      odd.push_back(S[i]);
    }
  }

  bool many0InEven = false;
  bool many1InEven = false;
  bool many0InOdd = false;
  bool many1InOdd = false;

  if (count(even, '0') >= count(even, '1')) {
    many0InEven = true;
  } else {
    many1InEven = true;
  }

  if (count(odd, '0') >= count(odd, '1')) {
    many0InOdd = true;
  } else {
    many1InOdd = true;
  }

  // cout << count(even, '0') << endl;
  // cout << count(even, '1') << endl;
  // cout << count(odd, '0') << endl;
  // cout << count(odd, '1') << endl;

  int result = 0;
  if (many0InEven) {
    if (many0InOdd) {
      // even:0 , odd: 0
      if (count(even, '0') >= count(odd, '0')) {
        result = count(odd, '0') + count(even, '1');
      } else {
        result = count(even, '0') + count(odd, '1');
      }
    } else {
      // even:0 , odd: 1
      if (count(even, '0') >= count(odd, '1')) {
        result = count(odd, '0') + count(even, '1');
      } else {
        result = count(even, '1') + count(odd, '0');
      }
    }
  } else {
    if (many0InOdd) {
      // even:1 , odd: 0
      if (count(even, '1') >= count(odd, '0')) {
        result = count(odd, '1') + count(even, '0');
      } else {
        result = count(even, '0') + count(odd, '1');
      }
    } else {
      // even:1 , odd: 1
      if (count(even, '1') >= count(odd, '1')) {
        result = count(odd, '1') + count(even, '0');
      } else {
        result = count(even, '1') + count(odd, '0');
      }
    }
  }

  cout << result << endl;

  return 0;
}
