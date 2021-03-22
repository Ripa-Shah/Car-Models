{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "uniform-windows",
   "metadata": {},
   "outputs": [],
   "source": [
    "game=[[0,0,0],\n",
    "     [0,0,0],\n",
    "     [0,0,0]]\n",
    "def game_board(game_map, player=0, row=0, column=0, just_display=False):\n",
    "    try:\n",
    "        print(\"0 1 2 \")\n",
    "        if not just_display:\n",
    "            game_map[row][column]=player\n",
    "            for count, row in enumerate(game_map):\n",
    "                print(count,row)\n",
    "            return game_map\n",
    "    except IndexError:\n",
    "        print(\"Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)\")\n",
    "        return False\n",
    "    except Exception as e:\n",
    "        print(str(e))\n",
    "        return False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "innocent-accuracy",
   "metadata": {},
   "outputs": [],
   "source": [
    "game=[[1,1,1],\n",
    "     [0,2,0],\n",
    "     [2,2,0]]\n",
    "\n",
    "def win(current_game):\n",
    "    for row in game:\n",
    "        print(row)\n",
    "        col1=row[0]\n",
    "        col2=row[1]\n",
    "        col3=row[2]\n",
    "        \n",
    "        if col1 == col2 == col3:\n",
    "            print(\"winner!!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "equipped-corner",
   "metadata": {},
   "outputs": [],
   "source": [
    "game = [[1,1,1],\n",
    "       [0,2,0],\n",
    "       [2,2,0]]\n",
    "def win(current_game):\n",
    "    for row in game:\n",
    "        print(row)\n",
    "        all_match=True\n",
    "        for item in row:\n",
    "            if item != row[0]:\n",
    "                all_match=False\n",
    "            if not all_match:\n",
    "                print(\"Winner\")\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "underlying-pulse",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "tender-wrestling",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(5, 10)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(5,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "attractive-printer",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "3\n",
      "6\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,10,3):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "quick-demand",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10\n",
      "-40\n",
      "-70\n"
     ]
    }
   ],
   "source": [
    "for i in range(-10,-100,-30):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "velvet-average",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 Mary\n",
      "1 had\n",
      "2 a\n",
      "3 little\n",
      "4 lamb\n"
     ]
    }
   ],
   "source": [
    "a = ['Mary', 'had', 'a', 'little', 'lamb']\n",
    "for i in range(len(a)):\n",
    "    print(i, a[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "closing-catch",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "agricultural-delivery",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 is a prime number\n",
      "4 equals 2 * 2\n",
      "5 is a prime number\n",
      "5 is a prime number\n",
      "5 is a prime number\n",
      "6 equals 2 * 3\n",
      "7 is a prime number\n",
      "7 is a prime number\n",
      "7 is a prime number\n",
      "7 is a prime number\n",
      "7 is a prime number\n",
      "8 equals 2 * 4\n",
      "9 is a prime number\n",
      "9 equals 3 * 3\n"
     ]
    }
   ],
   "source": [
    "for n in range(2,10):\n",
    "    for x in range(2,n):\n",
    "        if n%x==0:\n",
    "            print(n,\"equals\",x,\"*\",n//x)\n",
    "            break\n",
    "        else:\n",
    "            print(n,\"is a prime number\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "major-coating",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "found an even number 2\n",
      "found an odd number 3\n",
      "found an even number 4\n",
      "found an odd number 5\n",
      "found an even number 6\n",
      "found an odd number 7\n",
      "found an even number 8\n",
      "found an odd number 9\n"
     ]
    }
   ],
   "source": [
    "for num in range(2,10):\n",
    "    if num % 2 == 0:\n",
    "        print(\"found an even number\",num)\n",
    "        continue\n",
    "        \n",
    "    print(\"found an odd number\",num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "divided-president",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Print fibonnacci series upto n\n",
      "0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  \n"
     ]
    }
   ],
   "source": [
    "def fib(n):\n",
    "    print(\"Print fibonnacci series upto n\")\n",
    "    a, b=0, 1\n",
    "    while a<n:\n",
    "        print(a,end='  ')\n",
    "        a,b=b,a+b\n",
    "    print()\n",
    "\n",
    "fib(2000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "broke-serve",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fib2(n):\n",
    "    result=[]\n",
    "    a,b=0,1\n",
    "    while a<n:\n",
    "        result.append(a)\n",
    "        a,b=b,a+b\n",
    "    return result\n",
    "f100=fib2(100)\n",
    "f100\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ordinary-obligation",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ask_ok(prompt, retries=4, reminder='Please try again!'):\n",
    "    while True:\n",
    "        ok = input(prompt)\n",
    "        if ok in ('y','ye','yes'):\n",
    "            return True\n",
    "        if ok in ('n','no','nop','nope'):\n",
    "            return False\n",
    "        retries=retries-1\n",
    "        if retries < 0:\n",
    "            raise ValueError('Invalid user response')\n",
    "        print(reminder)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "gross-trick",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "i=5\n",
    "def f(arg=i):\n",
    "    print(arg)\n",
    "i=6\n",
    "f()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "collected-intermediate",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1, 2]\n",
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "def f(a,L=[]):\n",
    "    L.append(a)\n",
    "    return L\n",
    "print(f(1))\n",
    "print(f(2))\n",
    "print(f(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "clear-climb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(a, L=None):\n",
    "    if L is None:\n",
    "        L=[]\n",
    "        L.append(a)\n",
    "        return L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "stunning-wichita",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage,state='a stiff',action='voom',type='Norweign Blue'):\n",
    "    print(\"--This parrot wouldn\\'t \",action,end=' ')\n",
    "    print(\"If you put\",voltage,\"volts through it\")\n",
    "    print(\"Lovely plumage the\",type)\n",
    "    print(\"It\\'s\", state)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "encouraging-turkish",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "parrot() missing 1 required positional argument: 'voltage'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-1fa32faf15ff>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mparrot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: parrot() missing 1 required positional argument: 'voltage'"
     ]
    }
   ],
   "source": [
    "parrot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "mysterious-easter",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--This parrot wouldn't  voom If you put 1000 volts through it\n",
      "Lovely plumage the Norweign Blue\n",
      "It's a stiff\n"
     ]
    }
   ],
   "source": [
    "parrot(voltage=1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "sublime-costa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--This parrot wouldn't  VOOOOOM If you put 1000000 volts through it\n",
      "Lovely plumage the Norweign Blue\n",
      "It's a stiff\n",
      "--This parrot wouldn't  VOOOOOM If you put 1000000 volts through it\n",
      "Lovely plumage the Norweign Blue\n",
      "It's a stiff\n",
      "--This parrot wouldn't  jump If you put a million volts through it\n",
      "Lovely plumage the Norweign Blue\n",
      "It's bereft of life\n",
      "--This parrot wouldn't  voom If you put a thousand volts through it\n",
      "Lovely plumage the Norweign Blue\n",
      "It's pushing up the daisies\n"
     ]
    }
   ],
   "source": [
    "parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments\n",
    "parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments\n",
    "parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments\n",
    "parrot('a thousand', state='pushing up the daisies')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "corporate-albert",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "positional argument follows keyword argument (<ipython-input-30-2ac707ad11c1>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-30-2ac707ad11c1>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument\u001b[0m\n\u001b[1;37m                              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m positional argument follows keyword argument\n"
     ]
    }
   ],
   "source": [
    "parrot()                     # required argument missing\n",
    "parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument\n",
    "parrot(110, voltage=220)     # duplicate value for the same argument\n",
    "parrot(actor='John Cleese')  # unknown keyword argument"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "intended-bench",
   "metadata": {},
   "outputs": [],
   "source": [
    " def function(a):\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "metallic-kenya",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cheeseshop(kind, *arguments, **keywords):\n",
    "    print(\"-- Do you have any\", kind, \"?\")\n",
    "    print(\"-- I'm sorry, we're all out of\", kind)\n",
    "    for arg in arguments:\n",
    "        print(arg)\n",
    "    print(\"-\" * 40)\n",
    "    for kw in keywords:\n",
    "        print(kw, \":\", keywords[kw])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "temporal-bulgarian",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-- Do you have any Limburger ?\n",
      "-- I'm sorry, we're all out of Limburger\n",
      "It's very runny, sir.\n",
      "It's really very, VERY runny, sir.\n",
      "----------------------------------------\n",
      "shopkeeper : Michael Palin\n",
      "client : John Cleese\n",
      "sketch : Cheese Shop Sketch\n"
     ]
    }
   ],
   "source": [
    "cheeseshop(\"Limburger\", \"It's very runny, sir.\",\n",
    "           \"It's really very, VERY runny, sir.\",\n",
    "           shopkeeper=\"Michael Palin\",\n",
    "           client=\"John Cleese\",\n",
    "           sketch=\"Cheese Shop Sketch\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "logical-thickness",
   "metadata": {},
   "outputs": [],
   "source": [
    "def standard_arg(arg):\n",
    "    print(arg)\n",
    "\n",
    "def pos_only_arg(arg, /):\n",
    "    print(arg)\n",
    "\n",
    "def kwd_only_arg(*, arg):\n",
    "    print(arg)\n",
    "\n",
    "def combined_example(pos_only, /, standard, *, kwd_only):\n",
    "    print(pos_only, standard, kwd_only)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cooked-european",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3\n"
     ]
    }
   ],
   "source": [
    "combined_example(1, 2, kwd_only=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "severe-dragon",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3\n"
     ]
    }
   ],
   "source": [
    "combined_example(1, standard=2, kwd_only=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "dense-original",
   "metadata": {},
   "outputs": [],
   "source": [
    "def foo(name, **kwds):\n",
    "    return 'name' in kwds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "accredited-entrepreneur",
   "metadata": {},
   "outputs": [],
   "source": [
    "def foo(name, /, **kwds):\n",
    "    return 'name' in kwds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fuzzy-tenant",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "foo(1, **{'name': 2})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "biological-billy",
   "metadata": {},
   "outputs": [],
   "source": [
    "def write_multiple_items(file, separator, *args):\n",
    "    file.write(separator.join(args))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "amber-blocking",
   "metadata": {},
   "outputs": [],
   "source": [
    "def concat(*args, sep=\"/\"):\n",
    "    return sep.join(args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "rapid-baltimore",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'earth/mars/venus'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "concat(\"earth\", \"mars\", \"venus\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "relative-radar",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'earth.mars.venus'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "concat(\"earth\", \"mars\", \"venus\", sep=\".\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "adapted-politics",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(3, 6))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "exposed-madness",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "args=[3,10]\n",
    "list(range(*args))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "collective-velvet",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage, state='a stiff', action='voom'):\n",
    "    print(\"-- This parrot wouldn't\", action, end=' ')\n",
    "    print(\"if you put\", voltage, \"volts through it.\", end=' ')\n",
    "    print(\"E's\", state, \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "quarterly-dominant",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {\"voltage\": \"four million\", \"state\": \"bleedin' demised\", \"action\": \"VOOM\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "actual-arthur",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !\n"
     ]
    }
   ],
   "source": [
    "parrot(**d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "specified-folder",
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_incrementor(n):\n",
    "    return lambda x: x + n\n",
    "f = make_incrementor(42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "abstract-heater",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "advanced-ebony",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "43"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "boxed-swing",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]\n",
    ">>> pairs.sort(key=lambda pair: pair[1])\n",
    ">>> pairs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "nasty-energy",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "christian-tobacco",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.count('apple')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "continent-chair",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.count('tangerine')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "artificial-directive",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.index('banana')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "african-appendix",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.index('banana', 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "smoking-point",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "terminal-sound",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "random-sculpture",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits.append('grape')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "exceptional-withdrawal",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "solar-stick",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.sort()\n",
    "fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "personal-folks",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pear'"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "retained-benjamin",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "civic-protest",
   "metadata": {},
   "outputs": [],
   "source": [
    "stack = [3, 4, 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "widespread-leisure",
   "metadata": {},
   "outputs": [],
   "source": [
    "stack.append(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "numeric-watershed",
   "metadata": {},
   "outputs": [],
   "source": [
    "stack.append(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "related-danish",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 7]"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stack"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "sweet-probe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stack.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "forbidden-neutral",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stack"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "marked-longitude",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import deque"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "compliant-novel",
   "metadata": {},
   "outputs": [],
   "source": [
    "queue = deque([\"Eric\", \"John\", \"Michael\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "technological-volume",
   "metadata": {},
   "outputs": [],
   "source": [
    "queue.append(\"Terry\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "knowing-ceremony",
   "metadata": {},
   "outputs": [],
   "source": [
    "queue.append(\"Graham\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "psychological-georgia",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Eric'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "queue.popleft()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "smoking-closing",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "deque(['John', 'Michael', 'Terry', 'Graham'])"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "queue\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "registered-mambo",
   "metadata": {},
   "outputs": [],
   "source": [
    "squares = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "diverse-brunswick",
   "metadata": {},
   "outputs": [],
   "source": [
    "for x in range(10):\n",
    "    squares.append(x**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "modular-glory",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "variable-librarian",
   "metadata": {},
   "outputs": [],
   "source": [
    "squares = list(map(lambda x: x**2, range(10)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "governmental-fiber",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "apart-overhead",
   "metadata": {},
   "outputs": [],
   "source": [
    "combs=[]\n",
    "for x in [1,2,3]:\n",
    "    for y in [3,1,2]:\n",
    "        if x!=y:\n",
    "            combs.append((x,y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "marine-delivery",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 3), (1, 2), (2, 3), (2, 1), (3, 1), (3, 2)]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "combs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "ceramic-anatomy",
   "metadata": {},
   "outputs": [],
   "source": [
    "vec = [-4, -2, 0, 2, 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "abandoned-identification",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-8, -4, 0, 4, 8]"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x*2 for x in vec]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "printable-ambassador",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4]"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x for x in vec if x >= 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "extreme-myrtle",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 2, 0, 2, 4]"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[abs(x) for x in vec]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "capable-origin",
   "metadata": {},
   "outputs": [],
   "source": [
    "freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "soviet-hartford",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['banana', 'loganberry', 'passion fruit']"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[weapon.strip() for weapon in freshfruit]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "fantastic-chuck",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[(x, x**2) for x in range(6)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "insured-stroke",
   "metadata": {},
   "outputs": [],
   "source": [
    "vec = [[1,2,3], [4,5,6], [7,8,9]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "infectious-survey",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[num for elem in vec for num in elem]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "worst-design",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "retained-impact",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['3.1', '3.14', '3.142', '3.1416', '3.14159']"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[str(round(pi, i)) for i in range(1, 6)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "considerable-showcase",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = [\n",
    "    [1, 2, 3, 4],\n",
    "    [5, 6, 7, 8],\n",
    "    [9, 10, 11, 12],\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "designed-frontier",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-99-322d623b7f91>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;33m[\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmatrix\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-99-322d623b7f91>\u001b[0m in \u001b[0;36m<listcomp>\u001b[1;34m(.0)\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;33m[\u001b[0m\u001b[0mrow\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmatrix\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "[row[i] for row in matrix] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "italian-excitement",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[[row[i] for row in matrix] for i in range(4)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "coupled-possession",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "transposed = []\n",
    ">>> for i in range(4):\n",
    "...     transposed.append([row[i] for row in matrix])\n",
    "...\n",
    ">>> transposed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "sticky-value",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "transposed=[]\n",
    "for i in range(4):\n",
    "    transposed_row=[]\n",
    "    for row in matrix:\n",
    "        transposed_row.append(row[i])\n",
    "    transposed.append(transposed_row)\n",
    "transposed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "front-redhead",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<zip at 0x17ff4895f00>"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zip(*matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "communist-dealing",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(zip(*matrix))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "hispanic-knock",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[-1,1,66.25,333,333,1234.5]\n",
    "del a[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "bright-restriction",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 66.25, 333, 333, 1234.5]"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "brutal-powell",
   "metadata": {},
   "outputs": [],
   "source": [
    "del a[2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "tired-honolulu",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 66.25, 1234.5]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "stock-reality",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del a[:]\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "alert-nevada",
   "metadata": {},
   "outputs": [],
   "source": [
    "t=12345,54321,'hello!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "ranking-separate",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12345"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "under-camel",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12345, 54321, 'hello!')"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "clean-globe",
   "metadata": {},
   "outputs": [],
   "source": [
    "u=t,(1,2,3,4,44)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "according-accused",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((12345, 54321, 'hello!'), (1, 2, 3, 4, 44))"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "u"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "traditional-estimate",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-117-4e09c8e57631>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mt\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'00003'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "t[0]='00003'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "million-jimmy",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 2, 3), (3, 4, 2)]"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v=[(1,2,3),(3,4,2)]\n",
    "v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "atlantic-bearing",
   "metadata": {},
   "outputs": [],
   "source": [
    "empty=()\n",
    "singleton='hello'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "mighty-privilege",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(empty)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "dynamic-sodium",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(singleton)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "paperback-disability",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "singleton"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "possible-shepherd",
   "metadata": {},
   "outputs": [],
   "source": [
    "x,y,z=t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "powerful-edwards",
   "metadata": {},
   "outputs": [],
   "source": [
    " basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "sticky-announcement",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'banana', 'orange', 'apple', 'pear'}\n"
     ]
    }
   ],
   "source": [
    "print(basket)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "irish-eligibility",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " 'orange' in basket "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "alone-lemon",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'crabgrass' in basket"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "discrete-postcard",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = set('abracadabra')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "unlikely-tract",
   "metadata": {},
   "outputs": [],
   "source": [
    " b = set('alacazam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "pursuant-better",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'b', 'c', 'd', 'r'}"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "amino-duplicate",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'c', 'l', 'm', 'z'}"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "solar-philippines",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'b', 'd', 'r'}"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a-b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "textile-parking",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a|b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "eligible-samuel",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a', 'c'}"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a&b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "latin-mercy",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'b', 'd', 'l', 'm', 'r', 'z'}"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a^b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "ethical-youth",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = {x for x in 'abracadabra' if x not in 'abc'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "departmental-subscriber",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'d', 'r'}"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "enabling-ministry",
   "metadata": {},
   "outputs": [],
   "source": [
    "tel = {'jack': 4098, 'sape': 4139}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "naked-arbor",
   "metadata": {},
   "outputs": [],
   "source": [
    "tel['guido'] = 4127"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "uniform-thursday",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'jack': 4098, 'sape': 4139, 'guido': 4127}"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "imperial-fitness",
   "metadata": {},
   "outputs": [],
   "source": [
    "del tel['sape']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "radical-bhutan",
   "metadata": {},
   "outputs": [],
   "source": [
    "tel['irv'] = 4127"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "explicit-basic",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'jack': 4098, 'guido': 4127, 'irv': 4127}"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "thorough-collar",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['jack', 'guido', 'irv']"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(tel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "conditional-optimum",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['guido', 'irv', 'jack']"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(tel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "functioning-shark",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'guido' in tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "broadband-wheat",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'jack' not in tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "smart-finish",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sape': 4139, 'guido': 4127, 'jack': 4098}"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "proprietary-mauritius",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2: 4, 4: 16, 6: 36}"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "{x: x**2 for x in (2, 4, 6)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "structural-reaction",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'sape': 4139, 'guido': 4127, 'jack': 4098}"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict(sape=4139, guido=4127, jack=4098)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "conservative-knitting",
   "metadata": {},
   "outputs": [],
   "source": [
    " knights = {'gallahad': 'the pure', 'robin': 'the brave'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "round-contamination",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "gallahad the pure\n",
      "robin the brave\n"
     ]
    }
   ],
   "source": [
    "for k, v in knights.items():\n",
    "    print(k, v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "mathematical-performance",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 tic\n",
      "1 tac\n",
      "2 toe\n"
     ]
    }
   ],
   "source": [
    "for i, v in enumerate(['tic', 'tac', 'toe']):\n",
    "    print(i,v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "nervous-fifth",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name?  It is lancelot.\n",
      "What is your quest?  It is the holy grail.\n",
      "What is your favorite color?  It is blue.\n"
     ]
    }
   ],
   "source": [
    "questions = ['name', 'quest', 'favorite color']\n",
    "answers = ['lancelot', 'the holy grail', 'blue']\n",
    "for q, a in zip(questions, answers):\n",
    "    print('What is your {0}?  It is {1}.'.format(q, a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "cellular-chapel",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "7\n",
      "5\n",
      "3\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "for i in reversed(range(1,10,2)):\n",
    "    print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "fuzzy-luther",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "apple\n",
      "banana\n",
      "orange\n",
      "orange\n",
      "pear\n"
     ]
    }
   ],
   "source": [
    "basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']\n",
    "for i in sorted(basket):\n",
    "     print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "designed-start",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "orange\n",
      "pear\n"
     ]
    }
   ],
   "source": [
    "basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']\n",
    "for i in sorted(set(basket)):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "specialized-harvest",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[56.2, 51.7, 52.3, 56.7, 78.8]"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "row_data=[56.2,float('NaN'),51.7,52.3,float('NaN'),56.7,78.8]\n",
    "filtered_data=[]\n",
    "for value in row_data:\n",
    "    if not math.isnan(value):\n",
    "        filtered_data.append(value)\n",
    "filtered_data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "temporal-christianity",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fib(n):\n",
    "    a,b=0,1\n",
    "    while a<n:\n",
    "        print(a,end=' ')\n",
    "        a,b=b,a+b\n",
    "        print()\n",
    "def fib2(n):\n",
    "    results=[]\n",
    "    a,b=0,1\n",
    "    while a<n:\n",
    "        results.append(a)\n",
    "        a,b=b,a+b\n",
    "    return results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "automotive-novelty",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 \n",
      "1 \n",
      "1 \n",
      "2 \n",
      "3 \n",
      "5 \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0, 1, 1, 2, 3, 5]"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fib(7)\n",
    "fib2(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "acquired-dividend",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 1, 2, 3, 5]"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fib2(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "incorrect-restriction",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-182-eefe155c0e87>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mfibo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\fibo.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     59\u001b[0m   {\n\u001b[0;32m     60\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 61\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     62\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"continuous-branch\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     63\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import fibo\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "laden-adventure",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'fibo'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-175-eefe155c0e87>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mfibo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'fibo'"
     ]
    }
   ],
   "source": [
    "import fibo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "decreased-saturday",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-180-eefe155c0e87>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mfibo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\fibo.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     59\u001b[0m   {\n\u001b[0;32m     60\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 61\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     62\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"continuous-branch\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     63\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import fibo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "comparable-springfield",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'fibo' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-181-a6a8744949b5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfibo\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfib\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'fibo' is not defined"
     ]
    }
   ],
   "source": [
    "fibo.fib(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "varying-force",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '-f'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-183-62501033cb47>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;32mimport\u001b[0m \u001b[0msys\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mfib\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margv\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '-f'"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    import sys\n",
    "    fib(int(sys.argv[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "chinese-forwarding",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
