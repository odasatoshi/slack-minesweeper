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
        message.send(ms.generate_message())
        ms = Minesweeper(10, 0.2)
    message.send(ms.generate_message())
