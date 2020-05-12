# -*- coding: utf-8 -*-
import tkinter
import random

# ウィンドウ作成
root = tkinter.Tk()
root.title("王様げ〜む")
root.minsize(640, 480)
root.option_add("*font", ["MS Pゴシック", 22])

# 画像表示
canvas = tkinter.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
img = tkinter.PhotoImage(file="img3/test.png")
canvas.create_image(320, 240, image=img)

#テキスト表示
question = tkinter.Label(text="王様曰く", bg="white")
question.place(x=130, y=190)

question1 = tkinter.Label(text="人数：", bg="white")
question1.place(x=100, y=55)

# テキストボックス
entry = tkinter.Entry(width=4, bd=4)
entry.place(x=170, y=52)

#質問ボタン表示
askbutton = tkinter.Button(text="聞く")
askbutton.place(x=260, y=55)

# 答え表示
answer = tkinter.Label(text="……………　　　", bg="white")
answer.place(x=300, y=385)

answer1 = tkinter.Label(text="……………", bg="white")
answer1.place(x=155, y=385)

# イベント設定
def ask_click():
    val = entry.get()
    minutes = str(val)
    if minutes == "2":
        data = [1, 2]
        a, b = random.sample(data, 2)
        answer1["text"] = str(a) + "が" + str(b)
        foo = ["にキスする", "の乳首を舐める", "の服を1枚脱がす"]
        answer["text"] = str(random.choice(foo))
    elif minutes == "3":
        data = [1, 2, 3]
        a, b = random.sample(data, 2)
        answer1["text"] = str(a) + "が" + str(b)
        foo = ["にキスする", "の乳首を舐める", "の服を1枚脱がす"]
        answer["text"] = str(random.choice(foo))
    elif minutes == "4":
        data = [1, 2, 3, 4]
        a, b = random.sample(data, 2)
        answer1["text"] = str(a) + "が" + str(b)
        foo = ["にキスする", "の乳首を舐める", "の服を1枚脱がす"]
        answer["text"] = str(random.choice(foo))
    else:
        answer1["text"] = str("2~4人用です")
        answer["text"] = str("……………　　　")

askbutton["command"] = ask_click

# メインループ
root.mainloop()