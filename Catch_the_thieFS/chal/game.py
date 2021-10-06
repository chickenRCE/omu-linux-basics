#!/usr/bin/env python3
import os
import sys
import time
import random
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.par = None
        self.val = key
        self.id = -1

with open("names.txt", "r") as f:
    names = f.read().split('\n')
    random.shuffle(names)

def generate_tree(lvl):
    if not lvl:
        return None
    n = Node(names.pop())
    n.left = generate_tree(lvl-1)
    if n.left:
        n.left.par = n
    n.right = generate_tree(lvl-1)
    if n.right:
        n.right.par = n
    return n

# returns (Player, Thief)
def generate_ans(tree, r):
    if r == 1:
        l = [random.randint(0,1) for i in range(random.randint(2,3))]
        rob = tree
        for i in l:
            if i:
                rob = rob.left
            else:
                rob = rob.right
        return (tree, rob)
    elif r == 2:
        l = [random.randint(0,1) for i in range(3)]
        rob = tree
        for i in l:
            if i:
                rob = rob.left
            else:
                rob = rob.right
        if l[0]:
            return (tree.left, rob)
        else:
            return (tree.right, rob)
    elif r == 3:
        l = [random.randint(0,1) for i in range(3)]
        rob = tree
        for i in l:
            if i:
                rob = rob.left
            else:
                rob = rob.right
        if l[0]:
            return (rob, tree.left)
        else:
            return (rob, tree.right)
    elif r == 4:
        l = [random.randint(0,1) for i in range(3)]
        rob = tree
        for i in l:
            if i:
                rob = rob.left
            else:
                rob = rob.right
        if l[0]:
            return (rob, tree.right)
        else:
            return (rob, tree.left)
    elif r == 5:
        l = [random.randint(0,1) for i in range(random.randint(2,3))]
        rob = tree
        for i in l:
            if i:
                rob = rob.left
            else:
                rob = rob.right
        return (rob, rob.par)
    else:
        return (None, None)

def set_robb(robb, win):
    robb.val = "robb"
    win.addstr(coords[robb.id][0], coords[robb.id][1], "robb", curses.A_BOLD | curses.color_pair(1))

def set_root(root, win):
    root.val = "   / "
    win.addstr(coords[root.id][0], coords[root.id][1], "  / ")

def set_play(play, win):
    if "/" in play.val:
        win.addstr(coords[play.id][0], coords[play.id][1]+1, " / ", curses.A_BOLD | curses.color_pair(2))
    else:
        win.addstr(coords[play.id][0], coords[play.id][1], "play", curses.A_BOLD | curses.color_pair(2))

def check_answer(tree, play, robb, path):
    if path[0] == "/":
        path = path[1:]
        play = tree
    node = play
    for i in path:
        if i == "..":
            if node.par:
                node = node.par
        else:
            if node.left and node.left.val == i: 
                node = node.left
            elif node.right and node.right.val == i: 
                node = node.right
            else:
                return False
    if node.val == robb.val:
        return True
    else:
        return False

#print_tree(generate_tree(4))
# http://melvilletheatre.com/articles/ncurses-extended-characters/index.html

def splitall(path):
    path = os.path.normpath(path)
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

num_char = 0
limit = 25
def validator(ch):
    global num_char
    if ch == 10:
        return 7

    if ch not in [0x107, 0x14a]:
        num_char += 1
    else:
        num_char -= 1

    if num_char > limit:
        num_char = limit
        return None
    elif num_char < 0:
        num_char = 0

    stat.addstr(1,19, "{:02d}/{:02d}".format(num_char, limit))
    stat.refresh()
    return ch

coords = [(2+ 0, 2+4*6), (2+ 1, 2+4*6), # film apro
          (2+ 1, 2+4*4),                # sofa
          (2+ 3, 2+4*6), (2+ 4, 2+4*6), # milk lips
          (2+ 3, 2+4*4),                # neck
          (2+ 2, 2+4*2),                # goat
          (2+ 6, 2+4*6), (2+ 7, 2+4*6), # eyes belt
          (2+ 7, 2+4*4),                # swan
          (2+ 9, 2+4*6), (2+10, 2+4*6), # toes ribs
          (2+ 9, 2+4*4),                # hair
          (2+ 8, 2+4*2),                # fish
          (2+ 5, 2+4*0)]                # /

"""
                        film
                sofa    apro
        goat            
                neck    milk
                        lips
/
                        eyes
                swan    belt
        fish            
                hair    toes
                        ribs
"""

counter = 0
def print_tree(n, lvl, win):
    global counter
    if not n:
        return
    if n.left:
        print_tree(n.left, lvl+1, win)
    if n.right:
        print_tree(n.right,lvl+1, win)
    n.id = counter
    win.addstr(coords[counter][0], coords[counter][1], n.val)
    counter += 1

template = """
┌ Filesystem ──────────────────┐                                                                                      
│                              │                                                                                      
│                       20back │                                                                                      
│               20boat0050deer │                                                                                      
│       20nose004              │                                                                                      
│       1       30pipe0060flag │                                                                                      
│       1               30road │                                                                                      
│ gown004                      │                                                                                      
│       1               20oven │                                                                                      
│       1       20host0050taxi │                                                                                      
│       30lung004              │                                                                                      
│               30apro0060gift │                                                                                      
│                       30ball │                                                                                      
│                              │                                                                                      
└──────────────────────────────┘                                                                                      
""".split('\n')[1:-1]
template = [i.strip() for i in template]

stat = None
def main(stdscr):
    global stat, limit, num_char, counter

    # colours
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)

    # instructions
    ins = stdscr.subwin(15, 33, 0, 0)
    rectangle(ins, 0, 0, 14, 31)
    ins.addstr(0, 1, " Instructions ")
    ins.addstr(2, 8, "Catch the theiFS", curses.A_BOLD)
    ins.addstr(4, 3, "Navigate the filesystem(FS)")
    ins.addstr(5, 3, "to catch the thief")
    ins.addstr(5, 22, "robb", curses.color_pair(1))
    ins.addstr(7, 3, "The location of your player")
    ins.addstr(8, 3, "is indicated as ")
    ins.addstr(8, 19, "green", curses.color_pair(2))

    ins.addstr(11, 9, "Press any key", curses.A_BOLD)
    ins.addstr(12, 9, "to continue..", curses.A_BOLD)

    ins.refresh()
    stdscr.getch()
    ins.erase()

    # visualisation window
    vis = stdscr.subwin(15, 33, 0, 0)
    rectangle(vis, 0, 0, 14, 31)
    vis.addstr(0, 1, " Filesystem ")

    # status
    stat = stdscr.subwin(3, 33, 15, 0)
    rectangle(stat, 0, 0, 2, 31)
    stat.addstr(0, 1, " Round 1 of 5 ")
    stat.addstr(1, 2, "Characters used: ")
    stat.addstr(1,19, "00/{:02d}".format(limit))

    # edit window
    cmd = curses.newwin(3, 33, 18, 0)
    rectangle(cmd, 0, 0, 2, 31)
    cmd.addstr(0, 1, " Command ")
    cmd.addstr(1, 2, "cd")
    edit = curses.newwin(1, 26, 19, 5)
    box = Textbox(edit)

    # print tree lines
    chars = [curses.ACS_HLINE, curses.ACS_VLINE, curses.ACS_ULCORNER, curses.ACS_LLCORNER, curses.ACS_RTEE, curses.ACS_BTEE, curses.ACS_TTEE]
    i = 0; j = 0
    for line in template:
        for c in line:
            if c.isdigit():
                vis.addch(i, j, chars[int(c)])
            j += 1
        i += 1
        j  = 0

    stat.refresh()
    cmd.refresh()

    lims = [25, 20, 15, 10, 5]
    for r in range(1, 5+1):
        limit = lims[r-1]
        num_char = 0
        stat.addstr(0, 1, " Round {} of 5 ".format(r))
        stat.addstr(1,19, "00/{:02d}".format(limit))
        edit.erase()
        # Vis
        tree = generate_tree(4)
        play,robb = generate_ans(tree, r)
        counter = 0
        print_tree(tree, 0, vis)
        set_root(tree, vis)
        set_robb(robb, vis)
        set_play(play, vis)
        # Refresh
        stat.refresh()
        vis.refresh()
        edit.refresh()
        path = ""
        res = False
        while not res:
            if path:
                stat.addstr(1, 2, "Wrong Answer! Try again")
                stat.refresh()
                time.sleep(0.5)
                stat.addstr(1, 2, "Characters used:       ")
                stat.addstr(1,19, "{:02d}/{:02d}".format(num_char, limit))
                stat.refresh()
            # User input
            box.edit(validator)
            # Process input
            path = box.gather().strip()
            res = check_answer(tree, play, robb, splitall(path))

if __name__ == "__main__":
    # Disable traceback
    sys.tracebacklimit = 0 if len(sys.argv) == 1 else sys.tracebacklimit
    wrapper(main)
    print("Congratulations!")
    print("Here's the flag: \033[1momu{robb@crime:~$ cd /go/to/jail}\033[0m")
