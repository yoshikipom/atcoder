#include <iostream>
#include <queue>
using namespace std;

int main() {
  int N;
  cin >> N;
  std::priority_queue<int> que;
  int min_num = 1000000000;

  for (int i = 0; i < N; i++) {
    int tmp;
    cin >> tmp;
    if (min_num > tmp) {
      min_num = tmp;
    }
    que.push(tmp);
  }

  int max_num;
  while (!que.empty()) {
    max_num = que.top();
    // cout << min_num << endl;
    // cout << max_num << endl;
    while (que.top() == max_num && !que.empty()) {
      //   cout << "pop" << endl;
      que.pop();
    }
    if (max_num == min_num) {
      cout << min_num << endl;
      break;
    }
    int next_num = max_num - min_num;
    if (next_num < min_num) {
      min_num = next_num;
    }
    que.push(next_num);
    // cin >> N;
  }
}
