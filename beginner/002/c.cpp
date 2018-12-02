#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int xa, ya, xb, yb, xc, yc;
  std::cin >> xa >> ya >> xb >> yb >> xc >> yc;
  int a, b, c, d;
  a = xb - xa;
  b = yb - ya;
  c = xc - xa;
  d = yc - ya;
  // std::cout << a << b << c << d << '\n';
  double s = abs(a * d - b * c) / 2.0;
  std::cout << fixed << s << '\n';
  return 0;
}
