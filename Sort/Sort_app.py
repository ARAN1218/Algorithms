# -*- coding:utf-8 -*-
import tkinter
import time
import random

# キャンバスのサイズ
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600


# 描画時のウェイト（s）
WAIT = 0


class Sort():

    # ソート種類
    SELECTION_SORT = 1
    INSERT_SORT = 2
    BUBBLE_SORT = 3
    SHAKER_SORT = 4
    QUICK_SORT = 5
    MERGE_SORT = 6
    HEAP_SORT = 7

    def __init__(self, view):
        'ソートを行うオブジェクト生成'

        self.view = view

    def start(self, data, method):
        'ソートを開始'

        # ソートするデータのリストを設定
        self.data = data

        # ソートするデータの数を設定
        self.num = len(data)

        # 比較回数の初期化
        self.compare_num = 0

        # methodに応じてソートを実行
        if method == Sort.SELECTION_SORT:
            # 選択ソート実行
            self.selection_sort(0, self.num - 1)

        elif method == Sort.INSERT_SORT:
            # クイックソート実行
            self.insert_sort(0, self.num - 1)

        elif method == Sort.BUBBLE_SORT:
            # クイックソート実行
            self.bubble_sort(0, self.num - 1)

        elif method == Sort.SHAKER_SORT:
            # クイックソート実行
            self.shaker_sort(0, self.num - 1, True)

        elif method == Sort.QUICK_SORT:
            # クイックソート実行
            self.quick_sort(0, self.num - 1)

        elif method == Sort.MERGE_SORT:
            # マージソート用のワークメモリを用意
            self.work = [0] * self.num

            # マージソート実行
            self.merge_sort(0, self.num - 1)

        elif method == Sort.HEAP_SORT:
            # クイックソート実行
            self.heap_sort(0, self.num - 1)

        for num in self.data:
            print(num)

        # 比較回数を返却
        return self.compare_num

    def selection_sort(self, left, right):
        '選択ソートを実行'

        if left == right:
            # データ数１つなのでソート終了
            return

        # 最小値を仮で決定
        min = self.data[left]
        i_min = left

        # ソート範囲から最小値を探索
        for i in range(left, right + 1):

            if min > self.data[i]:
                # 最小値の更新
                min = self.data[i]
                i_min = i

            # 比較回数をインクリメント
            self.compare_num += 1

            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i_min])

        # 最小値と左端のデータを交換
        if i_min != left:
            # 交換必要な場合のみ交換
            self.data[left], self.data[i_min] = self.data[i_min], self.data[left]

        # 現在のデータの並びを表示
        #self.view.draw_data(self.data, point=[i_min])

        # 範囲を狭めて再度選択ソート
        self.selection_sort(left + 1, right)

    def insert_sort(self, left, right):
        if left == right+1:
            return

        left_index = self.data[left]
        for i in range(left+1):
            # 比較回数をインクリメント
            self.compare_num += 1

            if self.data[i] > self.data[left]:
                self.data[i], self.data[left] = self.data[left], self.data[i]

            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i])

        self.insert_sort(left+1, right)

    def bubble_sort(self, left, right):
        flag = False
        for i in range(right):
            # 比較回数をインクリメント
            self.compare_num += 1
            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i,i+1])
            if self.data[i] > self.data[i+1]:
                self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
                flag = True
        
        #self.view.draw_data(self.data, point=[i,i+1])
        if flag: self.bubble_sort(left, right-1)

    def shaker_sort(self, left, right, lr):
        flag = False

        if lr==True:
            for i in range(left,right):
                # 比較回数をインクリメント
                self.compare_num += 1
                # 現在のデータの並びを表示
                self.view.draw_data(self.data, point=[i,i+1])
                if self.data[i] > self.data[i+1]:
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
                    flag = True

            if flag: self.shaker_sort(left, right-1, False)
        else:
            for i in range(right,left,-1):
                # 比較回数をインクリメント
                self.compare_num += 1
                # 現在のデータの並びを表示
                self.view.draw_data(self.data, point=[i,i-1])
                if self.data[i] < self.data[i-1]:
                    self.data[i], self.data[i-1] = self.data[i-1], self.data[i]
                    flag = True

            if flag: self.shaker_sort(left+1, right, True)

    def quick_sort(self, left, right):
        'クイックソートを実行'

        if left >= right:
            # データ数１つ以下なのでソート終了
            return

        # pivot の決定
        pivot = self.data[left]

        i = left
        j = right

        # pivot以下の数字を配列の前半に、
        # pivot以上の数字を配列の後半に集める

        while True:
            # pivot以上の数字を左側から探索
            while self.data[i] < pivot:
                i += 1

                # 比較回数をインクリメント
                self.compare_num += 1

            # pivot以下の数字を右側から探索
            while self.data[j] > pivot:
                j -= 1

                # 比較回数をインクリメント
                self.compare_num += 1

            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i,j])

            # i >= j になったということは、
            # 配列の左側にpivot以下の数字が、
            # 配列の右側にpivot以上の数字が集まったということ
            if i >= j:
                # 集合の分割処理は終了
                break

            # 探索した２つの数字を交換
            tmp = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = tmp

            # 交換後の数字の次から探索再開
            i += 1
            j -= 1

        # 現在のデータの並びを表示
        self.view.draw_data(self.data, point=[])

        # 小さい数字を集めた範囲に対してソート
        self.quick_sort(left, i - 1)

        # 大きい数字を集めた範囲に対してソート
        self.quick_sort(j + 1, right)

    def merge_sort(self, left, right):
        'マージソートを実行'

        if left == right:
            # データ数１つなのでソート終了
            return

        # 集合を中央で２つに分割する
        mid = (left + right) // 2

        # 分割後の各集合のデータをそれぞれソートする
        self.merge_sort(left, mid)
        self.merge_sort(mid + 1, right)

        # ソート済みの各集合をマージする
        self.merge(left, mid, right)

        # 現在のデータの並びを表示
        self.view.draw_data(self.data, point=[])

    def merge(self, left, mid, right):
        '集合をマージする'

        # １つ目の集合の開始点をセット
        i = left

        # ２つ目の集合の開始点をセット
        j = mid + 1

        # マージ先集合の開始点をセット
        k = 0

        # ２つの集合のどちらかが、
        # 全てマージ済みになるまでループ
        while i <= mid and j <= right:

            # 比較回数をインクリメント
            self.compare_num += 1

            # マージ済みデータを抜いた２つの集合の、
            # 先頭のデータの小さい方をマージ
            if (self.data[i] < self.data[j]):

                self.work[k] = self.data[i]

                # マージした集合のインデックスと、
                # マージ先集合のインデックスをインクリメント
                i += 1
                k += 1
            else:
                self.work[k] = self.data[j]
                # マージした集合のインデックスと、
                # マージ先集合のインデックスをインクリメント
                j += 1
                k += 1

            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i,j])

        # マージ済みでないデータが残っている集合を、
        # マージ先集合にマージ
        while i <= mid:

            # 比較回数をインクリメント
            self.compare_num += 1

            self.work[k] = self.data[i]
            i += 1
            k += 1

        while j <= right:

            # 比較回数をインクリメント
            self.compare_num += 1

            self.work[k] = self.data[j]
            j += 1
            k += 1

        # マージ先集合をdataにコピー
        j = 0
        for i in range(left, right + 1):
            self.data[i] = self.work[j]
            j += 1

    def heap_sort(self, left, right):
        # array[n]をヒープ構成部(0～n-1)の最適な位置へ移動
        def upheap(array, n):
            while n != 0:
                # 比較回数をインクリメント
                self.compare_num += 1
                parent = int((n - 1) / 2)
                if array[n] > array[parent]:
                    # 親より大きな値の場合親子の値を交換
                    tmp = array[n]
                    array[n] = array[parent]
                    array[parent] = tmp
                    n = parent

                    # 現在のデータの並びを表示
                    self.view.draw_data(self.data, point=[n])
                else:
                    break

        # ルート[0]をヒープ(0～n)の最適な位置へ移動
        def downheap(array, n):
            if n == 0: return
            parent = 0
            while True:
                # 比較回数をインクリメント
                self.compare_num += 1

                child = 2 * parent + 1 # array[n]の子要素
                if child > n: break
                if (child < n) and array[child] < array[child + 1]:
                    child += 1
                if array[parent] < array[child]: # 子要素より小さい場合スワップ
                    tmp = array[child]
                    array[child] = array[parent]
                    array[parent] = tmp
                    parent = child; # 交換後のインデックスを保持
                    # 現在のデータの並びを表示
                    self.view.draw_data(self.data, point=[n])
                else:
                    break
        i = 0
        n = len(self.data)

        while(i < n):
            # ヒープを構成
            upheap(self.data, i)
            # 現在のデータの並びを表示
            #self.view.draw_data(self.data, point=[i])
            i += 1

        while(i > 1):
            # 比較回数をインクリメント
            self.compare_num += 1

            # ヒープから最大値を取り出し
            i -= 1
            self.data[i], self.data[0] = self.data[0], self.data[i]

            # 現在のデータの並びを表示
            self.view.draw_data(self.data, point=[i])

            # ヒープの再構成
            downheap(self.data, i-1)


class View():

    def __init__(self, master):
        'UI関連のオブジェクト生成'

        # 各種設定
        self.drawn_obj = []

        # キャンバスのサイズを決定
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT

        # 情報表示用のフレームを作成
        self.canvas_frame = tkinter.Frame(
            master,
        )
        self.canvas_frame.grid(column=1, row=1)

        # 操作用ウィジェットのフレームを作成
        self.operation_frame = tkinter.Frame(
            master,
        )
        self.operation_frame.grid(column=2, row=1, padx=10)

        # キャンバスの生成と配置
        self.canvas = tkinter.Canvas(
            self.canvas_frame,
            width=self.canvas_width,
            height=self.canvas_height,
        )
        self.canvas.pack()

        # ラベルの生成と配置
        self.text = tkinter.StringVar()
        self.text.set("開始ボタンを押してね")

        self.label = tkinter.Label(
            self.canvas_frame,
            textvariable=self.text,
        )
        self.label.pack()

        # テキストボックス配置用のフレームの生成と配置
        max_w = CANVAS_WIDTH // 2
        max_h = CANVAS_HEIGHT // 2
        if max_w < max_h:
            max = max_w
        else:
            max = max_h

        self.text_frame = tkinter.LabelFrame(
            self.operation_frame,
            text="データ数（最大" + str(max) + "）"
        )
        self.text_frame.pack(ipadx=10, pady=10)

        self.entry = tkinter.Entry(
            self.text_frame,
            width=4
        )
        self.entry.insert(0, max)
        self.entry.pack()

        # ラジオボタン配置用のフレームの生成と配置
        self.radio_frame = tkinter.LabelFrame(
            self.operation_frame,
            text="アルゴリズム"
        )
        self.radio_frame.pack(ipadx=10, pady=10)

        # チェックされているボタン取得用のオブジェクト生成
        self.sort = tkinter.IntVar()
        self.sort.set(Sort.QUICK_SORT)

        # アルゴリズム選択用のラジオボタンを３つ作成し配置
        self.selection_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="選択ソート",
            value=Sort.SELECTION_SORT
        )
        self.selection_button.pack()

        # アルゴリズム選択用のラジオボタンを３つ作成し配置
        self.insert_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="挿入ソート",
            value=Sort.INSERT_SORT
        )
        self.insert_button.pack()

        self.bubble_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="バブルソート",
            value=Sort.BUBBLE_SORT
        )
        self.bubble_button.pack()

        self.shaker_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="シェーカーソート",
            value=Sort.SHAKER_SORT
        )
        self.shaker_button.pack()

        self.quick_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="クイックソート",
            value=Sort.QUICK_SORT
        )
        self.quick_button.pack()

        self.merge_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="マージソート",
            value=Sort.MERGE_SORT
        )
        self.merge_button.pack()

        self.heap_button = tkinter.Radiobutton(
            self.radio_frame,
            variable=self.sort,
            text="ヒープソート",
            value=Sort.HEAP_SORT
        )
        self.heap_button.pack()

        # 開始ボタンの生成と配置
        self.button = tkinter.Button(
            self.operation_frame,
            text="開始",
        )
        self.button.pack()

    def start(self, n):
        '背景を描画'

        # データ数をセット
        self.num = n

        # １つのデータを表す線の幅を決定
        self.line_width = CANVAS_WIDTH / self.num

        # データの値１の線の高さを決定
        # データの値が N の時、線の高さは self.line_height * N となる
        self.line_height = CANVAS_HEIGHT / self.num

        # データ数が多すぎて描画できない場合
        if self.line_width < 2 or self.line_height < 2:
            return False

        # 背景位置調整用（中央寄せ）
        self.offset_x = int(
            (self.canvas.winfo_width() - self.line_width * self.num) / 2
        )
        self.offset_y = int(
            (self.canvas.winfo_height() - self.line_height * self.num + 1) / 2
        )

        # 一旦描画しているデータを削除
        for obj in self.drawn_obj:
            self.canvas.delete(obj)

        # 削除したので描画済みデータリストは空にする
        self.drawn_obj = []

        # 事前に背景オブジェクトを削除
        self.canvas.delete("background")

        # 背景を描画
        self.canvas.create_rectangle(
            self.offset_x,
            self.offset_y,
            int(self.offset_x + self.line_width * self.num),
            int(self.offset_y + self.line_height * self.num),
            width=0,
            fill="#EEEEFF",
            tag="background"
        )

        # 即座に描画を反映
        self.canvas.update()

        return True

    def get_algorithm(self):
        'ソートアルゴリズム取得'

        return self.sort.get()

    def get_data_num(self):
        'データ数取得'

        return int(self.entry.get())

    def draw_data(self, data, point=[]):
        'データの並びを線としてを描画'

        # 一旦描画しているデータを削除
        for obj in self.drawn_obj:
            self.canvas.delete(obj)

        # 削除したので描画済みデータリストは空にする
        self.drawn_obj = []

        # リストの数字を矩形で描画
        i = 0
        for p,value in enumerate(data):
            # 矩形の始点と終点を決定

            # データ位置から矩形の横方向座標を決定
            x1 = int(self.offset_x + i * self.line_width)
            x2 = int(self.offset_x + (i + 1) * self.line_width)

            # データの値から矩形の縦方向座標を決定
            y1 = int(self.offset_y + self.line_height * (self.num - value))
            y2 = int(self.offset_y + self.line_height * self.num)

            # 後から消せるようにtagをつけておく
            tag = "line" + str(i)
            self.drawn_obj.append(tag)

            # 長方形を描画
            self.canvas.create_rectangle(
                x1, y1,
                x2, y2,
                tag=tag,
                fill="#FFA588" if p not in point else "#5eff7e",
                width=1
            )

            i += 1

        # 描画を即座に反映
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
    def __init__(self, view, sort):
        'SortとViewを制御するオブジェクトを生成'

        # 制御するViewとSortのオブジェクト設定
        self.view = view
        self.sort = sort

        # ボタンクリック時のイベントを受け付け
        self.view.button["command"] = self.button_click

    def button_click(self):
        'ボタンクリック時の処理'

        num = self.view.get_data_num()
        # Viewの開始
        if not self.view.start(num):
            # メッセージ更新
            self.view.update_message(
                "データ数が多すぎます"
            )

            # 失敗したら何もしない
            return

        # NUMを最大値としたデータ数NUMの乱数リストを生成
        data = [random.randint(1, num-1) for i in range(num)]

        # メッセージ更新
        self.view.update_message("ソート中です")

        # ソートを開始
        compare_num = self.sort.start(data, self.view.get_algorithm())

        # メッセージ更新
        self.view.update_message(
            "ソート完了！（比較：" + str(compare_num) + "）"
        )


# アプリ生成
app = tkinter.Tk()
app.title("ソート")

# Viewオブジェクト生成
view = View(app)

# Sortオブジェクト生成
sort = Sort(view)

# Controllerオブジェクト生成
controller = Controller(view, sort)

# mainloopでイベント受付を待機
app.mainloop()
