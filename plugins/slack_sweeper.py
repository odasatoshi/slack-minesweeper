# coding: utf-8

from slackbot.bot import listen_to
from plugins.minesweep import Minesweeper

ms = Minesweeper(10, 0.2)
@listen_to('.*start.*')
def mention_func(message):
    global ms
    ms = Minesweeper(10, 0.2)
    message.send(ms.generate_message())

@listen_to('^\d{1},\d{1}$')
def listen_func(message):
    global ms
    row, col =  ms.shaping(message.body['text'])
    if ms.sweep(row, col) == False :
        ms.fullopen(row, col)
        die(message)
    message.send(ms.generate_message())
    if (ms.remnants() == 0):
        complete(message)
    else:
        message.send("あと、" + str(ms.remnants()) + "個掃除してください")

@listen_to('^f\d{1},\d{1}$')
def flag(message):
    global ms
    row, col = ms.shaping(message.body['text'][1:])
    ms.flag(row, col)
    message.send(ms.generate_message())

@listen_to('^lr\d{1},\d{1}$')
def left_right_click(message):
    global ms
    row, col = ms.shaping(message.body['text'][2:])
    if ms.left_right_click(row, col) == False :
        die(message)
    message.send(ms.generate_message())
    if (ms.remnants() == 0):
        complete(message)
    else:
        message.send("あと、" + str(ms.remnants()) + "個掃除してください")

def die(message):
    global ms
    message.send(ms.generate_message())
    message.send("あなたは死にました")
    ms = Minesweeper(10, 0.2)

def complete(message):
    global ms
    message.send("おめでとう")
    ms = Minesweeper(10, 0.2)
