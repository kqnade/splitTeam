def can_partition(levels):
    total = sum(levels)
    n = len(levels)
    target = total // 2

    # DPテーブルの初期化
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # DPテーブルの更新
    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i-1][j]
            if j >= levels[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-levels[i-1]]

    # チーム1の合計レベルを探す
    sum1 = 0
    for j in range(target, -1, -1):
        if dp[n][j]:
            sum1 = j
            break

    # チームのメンバーを割り当てる
    team1 = []
    team2 = []
    w = sum1
    for i in range(n, 0, -1):
        if not dp[i-1][w]:
            team1.append(levels[i-1])
            w -= levels[i-1]
        else:
            team2.append(levels[i-1])

    return team1, team2

levels = [3, 8, 2, 6, 4, 7, 5]
team1, team2 = can_partition(levels)
sum1 = sum(team1)
sum2 = sum(team2)

print(f"チーム1のメンバー: {team1}, 合計レベル: {sum1}")
print(f"チーム2のメンバー: {team2}, 合計レベル: {sum2}")
print(f"レベル差: {abs(sum1 - sum2)}")
