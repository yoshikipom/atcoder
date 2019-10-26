#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int x, y;
  std::cin >> x >> y;
  if (x > y) {
    std::cout << x << '\n';
  } else {
    std::cout << y << '\n';
  }
  return 0;
}
