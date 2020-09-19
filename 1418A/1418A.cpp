// Lukas und Paul 19.9.2020
#include <iostream>
#include <cmath>

long long clac(long long x, long long y, long long k){
  return (long long) std::ceil((long double)((y + 1) * k - 1) / (x - 1)) + k;
}

int main(){
  int t;
  std::cin >> t;
  for(int i = 0; i < t; ++i){
    long x;
    long y;
    long k;
    std::cin >> x;
    std::cin >> y;
    std::cin >> k;
    std::cout << clac(x, y, k) << std::endl;
  }
}
