import sys, math
from geo import distance

def main():
    data = sys.stdin.read().strip().split()
    x1, y1, x2, y2, r = map(float, data[:5])

    c = distance((x1, y1), (x2, y2))
    area = math.pi * (r ** 2)

    # 개행을 우리가 직접 제어: 마지막 줄에는 개행을 넣지 않는다
    sys.stdout.write(f"c = {c}\narea = {area}")
    # print() 사용 시 자동 개행이 추가될 수 있으므로 sys.stdout.write 사용

if __name__ == "__main__":
    main()
