N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
fish_lst = []
shark = [0, 0, 2, 0]  # i/ j/ size/ eat count/
# 먹을때마다 bfs 돌리기