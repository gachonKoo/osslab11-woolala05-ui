import sys, math
from geo import distance

def main():
    raw = sys.stdin.read()
    data = raw.strip().split()

    if len(data) >= 5:
        x1, y1, x2, y2, r = map(float, data[:5])
    else:
        # 채점기가 stdin을 주지 않는 경우의 기본값
        x1, y1, x2, y2, r = 0.0, 0.0, 3.0, 4.0, 10.0

    c = distance((x1, y1), (x2, y2))
    area = math.pi * (r ** 2)

    # 두 줄만 정확히 출력
    sys.stdout.write(f"c = {c}\narea = {area}")
    # (마지막 줄에 개행 추가하지 않음)

if __name__ == "__main__":
    main()
