#include <iomanip>
#include <iostream>

int getVV(double m) {
  if (m < 100) {
    return 0;
  } else if (100 <= m && m <= 5000) {
    return m / 100;
  } else if (6000 <= m && m <= 30000) {
    return m / 1000 + 50;
  } else if (35000 <= m && m <= 70000) {
    return (m / 1000 - 30) / 5 + 80;
  } else if (70 < m) {
    return 89;
  } else {
    return 0;
  }
}

int main(int argc, char const *argv[]) {
  double m;
  std::cin >> m;
  std::cout << std::setw(2) << std::setfill('0') << getVV(m) << "\n";
  return 0;
}
