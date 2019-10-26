#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int num;
  double result;
  std::cin >> num;
  for (size_t i = 1; i < num + 1; i++) {
    result += 10000.0 * i / num;
  }
  std::cout << result << '\n';
  return 0;
}
