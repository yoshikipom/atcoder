#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

double watch(double c, double r) { return 1.0 * (c + r) / 2.0; }

int main(int argc, char const *argv[]) {
  // input
  int N, K;
  std::cin >> N >> K;
  vector<double> movies;
  double movie;
  for (size_t i = 0; i < N; i++) {
    std::cin >> movie;
    movies.push_back(movie);
  }

  // process
  sort(movies.begin(), movies.end());

  double result = 0;
  for (size_t i = N - K; i < N; i++) {
    result = watch(result, movies[i]);
  }

  // output
  std::cout << fixed << setprecision(6) << result << '\n';
  return 0;
}
