# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import time
import random

# キャンバスのサイズ
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600

# 数値の定義
WALL = 0
PATH = 1
PASSED = 2
START = 3
GOAL = 4
NOW = 5
ROUTE = 6

# 色設定
PATH_COLOR = "white"
WALL_COLOR = "gray"
GOAL_COLOR = "red"
START_COLOR = "green"
PASSED_COLOR = "orange"
NOW_COLOR = "sky blue"
ROUTE_COLOR = "blue"



# 描画時のウェイト（s）
WAIT = 0.1

# 全探索アルゴリズムクラス
class Maze:

    DFS = 1
    BFS = 2

    def __init__(self, view):
        self.view = view
    
    def start(self, data, steps, method):
        '迷路探索を開始'
        self.maze = data
        self.steps = steps
        self.compare_num = 0

        # methodに応じて探索を実行
        if method == Maze.DFS:
            # 深さ優先探索実行
            self.dfs(self.maze, self.steps)

        elif method == Maze.BFS:
            # 幅優先探索実行
            self.bfs(self.maze, self.steps)

        # 比較回数・ゴールまでの道のりを返却
        return self.compare_num, self.way_to_goal_cnt

    # 上下左右の道を探索
    def search_point(self, p):
        tmp = []
        # 左方向の探索
        if self.maze[p[0]][p[1]-1] == 1:
            tmp.append([p[0], p[1]-1, "left"])

        # 上方向の探索
        if self.maze[p[0]-1][p[1]] == 1:
            tmp.append([p[0]-1, p[1], "up"])

        # 下方向の探索
        if self.maze[p[0]+1][p[1]] == 1:
            tmp.append([p[0]+1, p[1], "down"])

        # 右方向の探索
        if self.maze[p[0]][p[1]+1] == 1:
            tmp.append([p[0], p[1]+1, "right"])

        return tmp

    # 道順が小さくなる方向を探す関数
    def search_step(self, p):
        tmp = self.steps[p[0]][p[1]-1]
        p_tmp = [p[0], p[1]-1]
        if tmp > self.steps[p[0]-1][p[1]]:
            tmp = self.steps[p[0]-1][p[1]]
            p_tmp = [p[0]-1, p[1]]
        if tmp > self.steps[p[0]+1][p[1]]:
            tmp = self.steps[p[0]+1][p[1]]
            p_tmp = [p[0]+1, p[1]]
        if tmp > self.steps[p[0]][p[1]+1]:
            tmp = self.steps[p[0]][p[1]+1]
            p_tmp = [p[0], p[1]+1]

        self.steps[p_tmp[0]][p_tmp[1]] = 100000
        return p_tmp

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
        
        # ゴールまでの経路を求める(ゴールから逆順に進んでいく)
        maze[end_p[0]][end_p[1]] = 6
        p_to_goal = self.search_step(end_p)
        maze[p_to_goal[0]][p_to_goal[1]] = 6
        self.view.draw_data(maze)
        while True:
            p_to_goal = self.search_step(p_to_goal)
            maze[p_to_goal[0]][p_to_goal[1]] = 6
            self.view.draw_data(maze)
            if p_to_goal[0]==start_p[0] and p_to_goal[1]==start_p[1]:
                return 

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

        # ゴールまでの経路を求める(ゴールから逆順に進んでいく)
        maze[end_p[0]][end_p[1]] = 6
        p_to_goal = self.search_step(end_p)
        maze[p_to_goal[0]][p_to_goal[1]] = 6
        self.view.draw_data(maze)
        while True:
            p_to_goal = self.search_step(p_to_goal)
            maze[p_to_goal[0]][p_to_goal[1]] = 6
            self.view.draw_data(maze)
            if p_to_goal[0]==start_p[0] and p_to_goal[1]==start_p[1]:
                return 


class Home:

    def __init__(self, masters):
        'UI関連のオブジェクト生成'
        self.masters = masters

        # キャンバスのサイズを決定
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT

        # タイトルベージ --------------------------------------------------------------------
        # メインページフレーム作成
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # キャンバスの生成と配置
        self.main_canvas = tk.Canvas(
            self.main_frame,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
        )
        self.main_canvas.pack()

        # タイトルラベル作成
        self.titleLabel = tk.Label(self.main_canvas, text="Relax Algo", font=('Helvetica', '35'))
        self.titleLabel.place(anchor='center', x=CANVAS_WIDTH/2, y=CANVAS_HEIGHT/4)
        # ソートアルゴリズムに移動するボタン
        self.mazePageButton = tk.Button(self.main_canvas, text="ソートアルゴリズム(準備中)")
        self.mazePageButton.place(anchor='center', x=CANVAS_WIDTH/2, y=CANVAS_HEIGHT/2, width=300, height=50)
        # 全探索アルゴリズムに移動するボタン
        self.globalPageButton = tk.Button(self.main_canvas, text="全探索アルゴリズム", command=lambda : self.changePage(self.masters[1].main_frame))
        self.globalPageButton.place(anchor='center', x=CANVAS_WIDTH/2, y=CANVAS_HEIGHT/2+100, width=300, height=50)
        # 局所探索アルゴリズムに移動するボタン
        self.localPageButton = tk.Button(self.main_canvas, text="メタヒューリスティクス(準備中)")
        self.localPageButton.place(anchor='center', x=CANVAS_WIDTH/2, y=CANVAS_HEIGHT/2+200, width=300, height=50)

        #main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, frame):
        '画面遷移用の関数'
        frame.tkraise()

        # ------------------------------------------------------------------------------


class View:

    def __init__(self, master):
        'UI関連のオブジェクト生成'
        self.master = master

        # キャンバスのサイズを決定
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT

        # メイズページ -------------------------------------------------------------------
        # メイズページの下地を作る
        self.main_frame = tk.Frame(master)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # 情報表示用のフレームを作成
        self.canvas_frame = tk.Frame(
            self.main_frame,
        )
        self.canvas_frame.grid(column=1, row=1)

        # 操作用ウィジェットのフレームを作成
        self.operation_frame = tk.Frame(
            self.main_frame,
        )
        self.operation_frame.grid(column=2, row=1, padx=10)

        # キャンバスの生成と配置
        self.canvas = tk.Canvas(
            self.canvas_frame,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
        )
        self.canvas.pack()

        # ラベルの生成と配置
        self.text = tk.StringVar()
        self.text.set("開始ボタンを押してね")

        self.label = tk.Label(
            self.canvas_frame,
            textvariable=self.text,
        )
        self.label.pack()

        self.text_frame = tk.LabelFrame(
            self.operation_frame,
            text="迷路幅（最大51・奇数限定）"
        )
        self.text_frame.pack(ipadx=10, pady=10)

        self.entry = tk.Entry(
            self.text_frame,
            width=4
        )
        self.entry.insert(0, 21)
        self.entry.pack()

        # ラジオボタン配置用のフレームの生成と配置
        self.radio_frame = tk.LabelFrame(
            self.operation_frame,
            text="アルゴリズム"
        )
        self.radio_frame.pack(ipadx=10, pady=10)

        # チェックされているボタン取得用のオブジェクト生成
        self.algorithm = tk.IntVar()
        self.algorithm.set(Maze.BFS)

        # アルゴリズム選択用のラジオボタンを３つ作成し配置
        self.dfs_button = tk.Radiobutton(
            self.radio_frame,
            variable=self.algorithm,
            text="深さ優先探索",
            value=Maze.DFS
        )
        self.dfs_button.pack()

        # アルゴリズム選択用のラジオボタンを３つ作成し配置
        self.bfs_button = tk.Radiobutton(
            self.radio_frame,
            variable=self.algorithm,
            text="幅優先探索",
            value=Maze.BFS
        )
        self.bfs_button.pack()

        # 開始ボタンの生成と配置
        self.button = tk.Button(
            self.operation_frame,
            text="開始",
        )
        self.button.pack()

        # 戻るボタンの生成と配置
        self.mazeBackButton = tk.Button(
            self.operation_frame,
            text="メニューに戻る",
            command=lambda : self.changePage(home.main_frame)
        )
        self.mazeBackButton.pack()

        # 終了ボタンの生成と配置
        self.finish_button = tk.Button(
            self.operation_frame,
            text="終了",
            command=self.quit
        )
        self.finish_button.pack()

        # ------------------------------------------------------------------------

    def changePage(self, frame):
        '画面遷移用の関数'
        frame.tkraise()
    
    def quit(self):
        # 終了確認のメッセージ表示
        ret = messagebox.askyesno(
            title = "終了確認",
            message = "プログラムを終了しますか？")

        if ret == True:
            # 「はい」がクリックされたとき
            self.master.destroy()

    def start(self, n):
        '背景を描画'
        # データ数をセット
        self.num = n

        # データ数が多すぎる or データ数が奇数でない場合
        if self.num > 51 or self.num%2==0:
            return False

        # １つのデータを表す線の幅を決定
        self.line_width = CANVAS_WIDTH / self.num

        # データの値１の線の高さを決定
        # データの値が N の時、線の高さは self.line_height * N となる
        self.line_height = CANVAS_HEIGHT / self.num
        
        # 背景位置調整用（中央寄せ）
        self.offset_x = int(
            (self.canvas.winfo_width() - self.line_width * self.num) / 2
        )
        self.offset_y = int(
            (self.canvas.winfo_height() - self.line_height * self.num + 1) / 2
        )

        for j in range(self.num):
            for i in range(self.num):
                # 後から操作できるように座標に基づいたタグを付ける
                tag = "rectangle_" + str(i) + "_" + str(j)

                # キャンバスへの長方形の描画（迷路の描画）
                self.canvas.create_rectangle(
                    3 + i * CANVAS_WIDTH / self.num,
                    3 + j * CANVAS_HEIGHT / self.num,
                    3 + (i + 1) * CANVAS_WIDTH / self.num,
                    3 + (j + 1) * CANVAS_HEIGHT / self.num,
                    width=0,  # 枠線なし
                    tag=tag  # タグ
                )

        return True

    def get_algorithm(self):
        '探索アルゴリズム取得'

        return self.algorithm.get()

    def get_data_num(self):
        'データ数取得'
        return int(self.entry.get())
            

    def draw_data(self, maze):
        'データの並びを線としてを描画'
        for i in range(self.num):
            for j in range(self.num):
                # mazeリストの値に応じて色を取得
                if maze[j][i] == WALL:
                    color = WALL_COLOR
                elif maze[j][i] == PATH:
                    color = PATH_COLOR
                elif maze[j][i] == GOAL:
                    color = GOAL_COLOR
                elif maze[j][i] == START:
                    color = START_COLOR
                elif maze[j][i] == PASSED:
                    color = PASSED_COLOR
                elif maze[j][i] == NOW:
                    color = NOW_COLOR
                elif maze[j][i] == ROUTE:
                    color = ROUTE_COLOR
                else:
                    print("そんなマスはあり得ません")
                    return

                # (i,j)座標の長方形を特定するためにタグを作る
                tag = "rectangle_" + str(i) + "_" + str(j)

                # そのタグがつけられたfill設定を変更
                self.canvas.itemconfig(
                    tag,
                    fill=color
                )

        # 即座に描画を反映
        self.canvas.update()
        # WAIT秒分だけスリープ
        time.sleep(WAIT)

    def update_message(self, text):
        'メッセージを更新してラベルに表示'

        # ラベルに描画する文字列をセット
        self.text.set(text)

        # 描画を即座に反映
        self.label.update()



class Controller():
    def __init__(self, view, master):
        'MazeとViewを制御するオブジェクトを生成'

        # 制御するViewとMazeのオブジェクト設定
        self.view = view
        self.master = master

        # ボタンクリック時のイベントを受け付け
        self.view.button["command"] = self.button_click

    def button_click(self):
        'ボタンクリック時の処理'

        num = self.view.get_data_num()
        # Viewの開始
        if not self.view.start(num):
            # メッセージ更新
            self.view.update_message(
                "迷路幅が広すぎるか、偶数になっています"
            )

            # 失敗したら何もしない
            return

        # 迷路の初期化
        data =[[0 for column in range(num)] for row in range(num)]
        steps = [[100000 for column in range(num)] for row in range(num)]
        data[1][0] = 3
        data[len(data)-2][len(data)-1] = 4

        def make_maze(size, maze):
            # 探索点を保存
            init = [i-1 for i in range(1,size) if i%2==0]
            search_points = [[random.choice(init), random.choice(init)]]
            maze[search_points[0][0]][search_points[0][1]] = 1

            def anahori(s):
                tmp = []
                # 上方向の探索
                if 0 <= s[0]-2 <= size-1: # 迷路の座標に収まっているか
                    if maze[s[0]-1][s[1]] == maze[s[0]-2][s[1]] == 0: # 迷路が既に掘られていないか
                        tmp.append([s[0]-1, s[1], s[0]-2, s[1]])

                # 右方向の探索
                if 0 <= s[1]+2 <= size-1: # 迷路の座標に収まっているか
                    if maze[s[0]][s[1]+1] == maze[s[0]][s[1]+2] == 0: # 迷路が既に掘られていないか
                        tmp.append([s[0], s[1]+1, s[0], s[1]+2])

                # 下方向の探索
                if 0 <= s[0]+2 <= size-1: # 迷路の座標に収まっているか
                    if maze[s[0]+1][s[1]] == maze[s[0]+2][s[1]] == 0: # 迷路が既に掘られていないか
                        tmp.append([s[0]+1, s[1], s[0]+2, s[1]])

                # 左方向の探索
                if 0 <= s[1]-2 <= size-1: # 迷路の座標に収まっているか
                    if maze[s[0]][s[1]-1] == maze[s[0]][s[1]-2] == 0: # 迷路が既に掘られていないか
                        tmp.append([s[0], s[1]-1, s[0], s[1]-2])

                return tmp

            # 一次探索開始
            for s in search_points:
                tmp = anahori(s)
                if tmp:
                    cs = random.choice(tmp)
                    maze[cs[0]][cs[1]], maze[cs[2]][cs[3]] = 1, 1
                    search_points.append([cs[2], cs[3]])

            # 二次探索開始
            while search_points:
                s = random.choice(search_points)
                search_points.remove(s)
                tmp = anahori(s)
                if tmp:
                    t = random.choice(tmp)
                    maze[t[0]][t[1]], maze[t[2]][t[3]] = 1, 1
                    if tmp:
                        search_points.append([t[2], t[3]])
                        search_points.append(s)

        make_maze(num, data)

        # メッセージ更新
        self.view.update_message("探索中です...")

        # ソートを開始
        compare_num, way_to_goal_cnt = self.master.start(data, steps, self.view.get_algorithm())

        # メッセージ更新
        self.view.update_message(
            "探索完了！（比較回数：" + str(compare_num) + ", ゴールまでの距離：" + str(way_to_goal_cnt) + "）"
        )


# アプリ生成
app = tk.Tk()
app.title("Relax Algo")

# Viewオブジェクト生成
view_maze = View(app)
home = Home([0, view_maze, 2])

# Mazeオブジェクト生成
#maze = maze(view)
# Mazeオブジェクト生成
maze = Maze(view_maze)
# TSPオブジェクト生成
#tsp = TSP(view)

# Controllerオブジェクト生成
controller = Controller(view_maze, maze)

# mainloopでイベント受付を待機
app.mainloop()
