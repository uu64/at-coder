# -*- coding: utf-8 -*-

def move(now, goal, nodes, counter, history, result):
    now = i
    for i in range(len(nodes)):
        if nodes[i] == 0:
            continue
        else:
            next_node = i
            print("node: {}, counter: {}".format(now, counter))
            if counter == 3:
                counter = 0
                if now in history:
                    # すでに移動済
                    return

                history.append(now)

                if now == goal:
                    # ゴールに到着
                    result.append(len(history))
                    print(history)
                    return

        move(now, goal, graph[now], counter+1, history, result)

N, M = map(int, input().split())

graph = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

S, T = map(int, input().split())

# グラフを距離3に変換する
for i in range(M):
    for j in range(M):
        if graph[i][j] == 0:
            continue
        else:


# history = []
# result = []

# # インデックスと合わせる
# S -= 1
# T -= 1

# for nodes in graph:
#     print(nodes)

# now = S
# counter = 0
# history.append(now)
# move(now, T, graph[now], counter, history, result)


# print(result)