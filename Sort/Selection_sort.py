import pygame
from pygame.locals import *
import sys
import random

def selection_sort(datalist, swaplist):
    for x in range(0, len(datalist)):
        tmp = x
        for y in range(x, len(datalist)):
            if datalist[tmp] >= datalist[y]:
                tmp = y
        swaplist.append([x, tmp])
        datalist[x], datalist[tmp] = datalist[tmp], datalist[x]
# 単純選択ソートの実装


def main():
    MYUPDATE = 26  # ユーザー定義イベントの番号を設定
    windowsize = (1280, 720)
    pygame.init()  # ライブラリの初期化
    # フォントの用意
    # print(pygame.font.get_fonts())  # 使えるフォントの一覧を表示する
    font1 = pygame.font.SysFont("msgothicmsuigothicmspgothic", 40)

    # テキストの設定
    text1 = font1.render("Selection Sort", True, (0, 0, 0))
    screen = pygame.display.set_mode(windowsize)  # 画面サイズを指定
    pygame.display.set_caption("Sample of Sorting algorithm")  # ウィンドウタイトルを設定
    clock = pygame.time.Clock()
    changelist = []

    xmargin = 50
    ymargin = 50
    datasize = 210
    vals = list(range(1, datasize+1))
    random.shuffle(vals)

    dwidth = int((windowsize[0]-xmargin*2) / datasize)
    fdwidth = float(windowsize[0]-xmargin*2) / datasize
    print(dwidth)
    yspan = windowsize[1] - ymargin
    backrect = [[100, 100, 100], pygame.Rect(50, 50, windowsize[0]-xmargin*2, windowsize[1]-ymargin*2), 0]
    datalist = []
    for i in range(datasize):
        tval = (float(vals[i]) / datasize) * (windowsize[1] - ymargin * 2)
        inrect = [[0, 0, 0], pygame.Rect(xmargin + (i * fdwidth), yspan - tval, dwidth, tval), 1]
        outrect = [[80, 80, 80], pygame.Rect(xmargin + (i * fdwidth), yspan - tval, dwidth, tval), 0]
        datalist.append([inrect, outrect])
        pygame.time.set_timer(MYUPDATE, 100)  # 100msごとにユーザー定義イベントを発生させる

    selection_sort(vals, changelist)  # ソートの実行
    print(vals)
    anistate = -1 # -1 初期状態　0 描画準備状態 1 選択　2 交換 描画の状態を表す
    while True:
        for event in pygame.event.get():  # 終了イベントの処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                anistate = 0
            if event.type == MYUPDATE:
                if len(changelist) != 0:
                    if anistate == 0:
                        tmp = changelist.pop(0)
                        datalist[tmp[0]][1][0] = [255, 0, 0]
                        datalist[tmp[1]][1][0] = [0, 0, 255]
                        anistate = 1
                    elif anistate == 1:
                        datalist[tmp[0]][1][1].h, datalist[tmp[1]][1][1].h = datalist[tmp[1]][1][1].h, datalist[tmp[0]][1][1].h
                        datalist[tmp[0]][1][1].y, datalist[tmp[1]][1][1].y = datalist[tmp[1]][1][1].y, datalist[tmp[0]][1][1].y
                        datalist[tmp[0]][0][1].h, datalist[tmp[1]][0][1].h = datalist[tmp[1]][0][1].h, datalist[tmp[0]][0][1].h
                        datalist[tmp[0]][0][1].y, datalist[tmp[1]][0][1].y = datalist[tmp[1]][0][1].y, datalist[tmp[0]][0][1].y
                        datalist[tmp[1]][1][0] = [80, 80, 80]
                        datalist[tmp[0]][1][0] = [0, 255, 0]
                        pygame.display.update()  # 画面の更新
                        anistate = 0
                else:
                    datalist[tmp[1]][1][0] = [80, 80, 80]
                    datalist[tmp[0]][1][0] = [0, 255, 0]
        screen.fill((203, 255, 135))  # 画面を指定色（R,G,B)で塗りつぶし
        pygame.draw.rect(screen, backrect[0], backrect[1], backrect[2])
        for trect in datalist:
            pygame.draw.rect(screen, trect[1][0], trect[1][1], trect[1][2])
            pygame.draw.rect(screen, trect[0][0], trect[0][1], trect[0][2])
        screen.blit(text1, (50, 5))
        pygame.display.update()  # 画面の更新
        clock.tick(60)


if __name__ == "__main__":
    main()
