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

class Problem {
 public:
  int point;
  int problemCount;
  int complete;
  int all_point;
  int rate;
  bool operator<(const Problem &another) const { return rate > another.rate; };
};

void disp(vector<Problem *> problems) {
  for (Problem *p : problems) {
    cout << "problems: " << p->point << "point" << endl;
    cout << p->problemCount << endl;
    cout << p->complete << endl;
    cout << p->all_point << endl;
    cout << p->rate << endl;
  }
}

int main() {
  int D, G;
  cin >> D >> G;
  vector<Problem *> problems;
  rep(i, D) {
    int p, c;
    cin >> p >> c;
    Problem *problem = new Problem;
    int point = (i + 1) * 100;
    problem->point = point;
    problem->complete = c;
    problem->problemCount = p;
    int all_point = point * p + c;
    problem->all_point = all_point;
    problem->rate = all_point / p;
    problems.push_back(problem);
  }

  // コストパフォーマンスがいい順番に並べる
  sort(problems.rbegin(), problems.rend());

  disp(problems);

  int result = 0;
  int remained = G;
  int lastProblemIndex = D - 1;

  // 全部とく問題を処理
  rep(i, D) {
    if (problems[i]->all_point <= remained) {
      remained -= problems[i]->all_point;
      result += problems[i]->problemCount;
      // cout << "i " << i << " result " << result << " remained " << remained
      //  << endl;
      continue;
    } else {
      lastProblemIndex = i;
      break;
    }
  };

  // 最後の問題を処理

  if (remained != 0) {
    int lastSolveCount = INF;
    for (int i = lastProblemIndex; i < D; i++) {
      int solveCount = remained / problems[i]->point;
      if (remained % problems[i]->point != 0) {
        solveCount++;
      }
      lastSolveCount = min(lastSolveCount, solveCount);
    }
    result += lastSolveCount;

    remained -= problems[lastProblemIndex]->point * lastSolveCount;
    if (remained > 0) {
      cout << "remained = " << remained << endl;
    }

    remained = 0;
  }

  cout << result << endl;

  return 0;
}
