# 深さ優先探索
def dfs(self, maze, steps):
    start_p = [1,1]
    end_p = [len(maze)-2, len(maze)-2]
    maze[start_p[0]][start_p[1]] = 2
    steps[start_p[0]][start_p[1]] = 1
    p_pre = start_p
    ps = self.search_point(start_p)
    # 比較回数をインクリメント
    self.compare_num += 1

    # 探索開始
    while True:
        p = ps.pop()
        maze[p[0]][p[1]] = 2
        steps[p[0]][p[1]] = steps[p_pre[0]][p_pre[1]] + 1
        p_pre = p
        self.view.draw_data(maze)
        if p[0]==end_p[0] and p[1]==end_p[1]: # ゴールに辿り着いた
            self.way_to_goal_cnt = steps[end_p[0]][end_p[1]]
            break
        else:
            ps_tmp = self.search_point(p)
            # 比較回数をインクリメント
            self.compare_num += 1
            if ps_tmp:
                ps += ps_tmp
