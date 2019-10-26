#include <iostream>
#include <vector>
using namespace std;

typedef long long int ll;

long nCr(ll n, ll r) {
  vector<ll> v1, v2;
  v2.push_back(1);
  for (size_t i = 0; i < n; i++) {
    v1 = v2;
    for (size_t i = 0; i < v1.size() - 1; i++) {
      v2[i + 1] = (v1[i] + v1[i + 1]) % 1000000007;
    }
    v2.push_back(1);
    // for (ll i : v2) {
    //   std::cout << i << ',';
    // }
    // std::cout << '\n';
  }

  return v2[r];
}

int main(int argc, char const *argv[]) {
  // nCr(100, 1);
  int R, C, X, Y, D, L;
  std::cin >> R >> C >> X >> Y >> D >> L;
  // how main area
  ll area_num = (R - X + 1) * (C - Y + 1);
  ll things_num = nCr(D + L, D);

  // std::cout << area_num << ':' << things_num << '\n';

  ll result = (area_num * things_num) % 1000000007;

  // output
  std::cout << result << '\n';
  return 0;
}
