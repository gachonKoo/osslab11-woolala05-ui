from geo import distance, midpoint, slope, triangle_area, rectangle_area

def main():
    p1, p2, p3 = (0, 0), (3, 4), (3, 0)
    print("distance(p1, p2) =", distance(p1, p2))        # 5.0
    print("midpoint(p1, p2) =", midpoint(p1, p2))        # (1.5, 2.0)
    print("triangle_area(p1,p2,p3) =", triangle_area(p1, p2, p3))  # 6.0
    print("rectangle_area(3,4) =", rectangle_area(3, 4)) # 12.0
    try:
        print("slope(p1,p3) =", slope(p1, p3))           # 0.0
    except ZeroDivisionError as e:
        print("slope undefined:", e)

if __name__ == "__main__":
    main()
