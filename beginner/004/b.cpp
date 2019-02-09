#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[]) {
  char v[4][4];
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      char c;
      cin >> c;
      if (c == '\n') continue;
      v[i][j] = c;
    }
  }

  for (int i = 3; i > -1; i--) {
    for (int j = 3; j > -1; j--) {
      cout << v[i][j] << ' ';
    }
    cout << '\n';
  }
  return 0;
}
