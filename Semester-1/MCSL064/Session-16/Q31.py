def polynomial_sum(p1:list[int], p2:list[int]) -> list[int]:
    m, n = len(p1), len(p2)
    size = max(m, n)
    poly_sum = [0] * size

    for i in range(m):
        poly_sum[i] = p1[i]

    for j in range(n):
        poly_sum[j] += p2[j]

    return poly_sum

if __name__ == "__main__":
    input_p1 = [5, 0, 10, 6]
    input_p2 = [1, 2, 4]
    print(polynomial_sum(input_p1, input_p2))