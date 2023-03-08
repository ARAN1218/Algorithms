    # 幅優先探索
    def bfs(self, maze, steps):
        start_p = [1,1]
        end_p = [len(maze)-2, len(maze)-2]
        move_to_return = {"up":[1,0], "right":[0,-1], "down":[-1,0], "left":[0,1]}
        maze[start_p[0]][start_p[1]] = 2
        steps[start_p[0]][start_p[1]] = 1
        ps = self.search_point(start_p)
        # 比較回数をインクリメント
        self.compare_num += 1

        while True:
            p = ps.pop(0)
            steps[p[0]][p[1]] = steps[p[0]+move_to_return[p[2]][0]][p[1]+move_to_return[p[2]][1]] + 1
            maze[p[0]][p[1]] = 2
            self.view.draw_data(maze)
            if p[0]==end_p[0] and p[1]==end_p[1]: # ゴールに辿り着いた
                self.way_to_goal_cnt = steps[end_p[0]][end_p[1]]
                break
            else:
                ps_tmp = self.search_point(p)
                # 比較回数をインクリメント
                self.compare_num += 1
                if len(ps_tmp) > 0:
                    ps += ps_tmp
