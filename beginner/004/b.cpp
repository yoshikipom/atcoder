#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[]) {
  char v[4][4];
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 4; j++) {
      char c;
      cin.get(c);
      if (c == '\n')
        continue;
      v[i][j] = c;
      std::cout << i << ":" << j << '\n';
    }
  }

  std::cout << v[3][0] << '\n';
  return 0;
}
