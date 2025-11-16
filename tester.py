import sys, math
from geo import distance

def main():
    data = sys.stdin.read().strip().split()
    # 기대 입력: x1 y1 x2 y2 r  (여분 입력이 와도 앞의 5개만 사용)
    x1, y1, x2, y2, r = map(float, data[:5])

    c = distance((x1, y1), (x2, y2))           # 두 점 사이 거리
    area = math.pi * (r ** 2)                   # 원의 넓이

    # 정확히 기대하는 형식으로 출력 (공백/대소문자/등호 위치 주의)
    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
