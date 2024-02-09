# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import random

#ここにタスクの内容
task=[
    "ChatGPTでアニメ反応集",
    "画像生成して睡眠動画作成",
    "ショート動画作成",
    "イラスト作成",
    "Pairs",
    "JavaSilverの資格勉強",
    "Gitの使い方勉強",
    "Java8のとJava5の違い"]

layout = [  
    [sg.Text('今から行うタスクを決めます', font=("Helvetica", 16))],
    [sg.Text('ボタンを押してガチャを回してください', font=("Helvetica", 16))],
    [[sg.Text(f"・{taskList}")] for taskList in task],
    [sg.Text('60:00', font=("Helvetica", 20), key='-TIMER-')],
    [sg.B('タスクガチャ'), sg.B('スタート', key='-START-'), sg.B('ストップ', key='-STOP-'), sg.Push()],
    [sg.Multiline(size=(60,15), font=("Helvetica", 25), key='-result-')]
]

window = sg.Window('タスクガチャ', layout, size=(700, 500))

def gen_character():
    # ret="\n\n" #改行を追加したいときは
    ret=random.choice(task)
    return ret

last_task = ""
timer_running = False
start_time = 60 * 60  # 60分

while True:
    # タイマーが動いている場合は1秒ごとに更新
    event, values = window.read(timeout=1000 if timer_running else None)  
    if event == sg.WIN_CLOSED: 
        break

    if event == 'タスクガチャ':
        new_task = gen_character()
        while new_task == last_task:
            new_task = gen_character()
        # 画面を更新し、新しいテキストが一番上にくるようにする
        current_text = window['-result-'].get()  # 現在の内容を取得
        window['-result-'].update(value=new_task + current_text)  # 新しいテキストを先頭に追加
        last_task = new_task  # 更新されたタスクを保持

    if event == '-START-':
        timer_running = True
    
    if event == '-STOP-':
        timer_running = False
    
    if timer_running:
        start_time -= 1      # 1秒減らす
        if start_time <= 0:  # タイマーが0になったら停止
            timer_running = False
            start_time = 0
        mins, secs = divmod(start_time, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        window['-TIMER-'].update(time_format)

window.close()