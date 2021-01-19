def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장합니다.
    total_height = 0

    # 리스트의 각 인덱스를 돌면서 해당 칸에 담기는 빗물의 양을 구합니다.
    # 0번 인덱스와 마지막 인덱스는 볼 필요가 없습니다.
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구합니다.
        left_max = max(buildings[:i])
        right_max = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(left_max, right_max)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
