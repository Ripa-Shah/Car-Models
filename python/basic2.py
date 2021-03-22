{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "indonesian-toyota",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s=\"Hello World\"\n",
    "str(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "informal-magnitude",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"'Hello World'\""
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "repr(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "third-cleaner",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0.14285714285714285'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(1/7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ideal-norwegian",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of pi is approximately3.142.\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "print(f'The value of pi is approximately{math.pi:.3f}.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "expanded-atlanta",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sjoered    ==>       4127\n",
      "Jack       ==>       4098\n",
      "Dcab       ==>       7678\n"
     ]
    }
   ],
   "source": [
    "table={'sjoered':4127,'Jack':4098,'Dcab':7678}\n",
    "for name, phone in table.items():\n",
    "    print(f'{name:10} ==> {phone:10d}')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "restricted-socket",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My hovercraft is full of eels.\n"
     ]
    }
   ],
   "source": [
    "animals = 'eels'\n",
    "print(f'My hovercraft is full of {animals}.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "impaired-pillow",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we are the Knights who say Ni!\n"
     ]
    }
   ],
   "source": [
    "print('we are the {} who say {}!'.format('Knights','Ni'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "adapted-consortium",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "spam and eggs\n"
     ]
    }
   ],
   "source": [
    "print('{0} and {1}'.format('spam', 'eggs'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "selected-consent",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eggs and spam\n"
     ]
    }
   ],
   "source": [
    "print('{1} and {0}'.format('spam','eggs'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "polyphonic-innocent",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This spam is absolutely horrible\n"
     ]
    }
   ],
   "source": [
    "print('This {food} is {adjective}'.format( food='spam', adjective='absolutely horrible'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "monthly-elder",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The story of Bill,Marfred and George.\n"
     ]
    }
   ],
   "source": [
    "print('The story of {0},{1} and {other}.'.format('Bill','Marfred',other='George'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "southeast-angola",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jack: 4098; Sjoerd: 4127; Dcab: 8637678\n"
     ]
    }
   ],
   "source": [
    "table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}\n",
    "print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '\n",
    "      'Dcab: {0[Dcab]:d}'.format(table))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "sustainable-tractor",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jack: 4098; Sjoerd: 4127; Dcab: 8637678\n"
     ]
    }
   ],
   "source": [
    "print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "running-flashing",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1   1    1\n",
      " 2   4    8\n",
      " 3   9   27\n",
      " 4  16   64\n",
      " 5  25  125\n",
      " 6  36  216\n",
      " 7  49  343\n",
      " 8  64  512\n",
      " 9  81  729\n",
      "10 100 1000\n"
     ]
    }
   ],
   "source": [
    "for x in range(1, 11):\n",
    "    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "auburn-arctic",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1   1  2   4  3   9  4  16  5  25  6  36  7  49  8  64  9  81 10 100 "
     ]
    }
   ],
   "source": [
    "for x in range(1, 11):\n",
    "    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "coupled-gilbert",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000\n"
     ]
    }
   ],
   "source": [
    "print(repr(x*x*x).rjust(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "russian-omega",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'00012'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'12'.zfill(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ambient-transcript",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'-003.14'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'-3.14'.zfill(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "addressed-forest",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of pi is approximately 3.142.\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "print('The value of pi is approximately %5.3f.' % math.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "arabic-economy",
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('workfile', 'w')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "alpha-april",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('workfile') as f:\n",
    "    read_data = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "threatened-monster",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " f.closed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "oriented-representation",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-f25c033ac067>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "for line in f:\n",
    "    print(line, end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "sophisticated-interview",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-7e1d2e12b839>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    " f.readline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "passing-sterling",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-cc42235461d2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'This is a test\\n'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "f.write('This is a test\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "simplified-michigan",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-31-ed08d1bc4d2e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m'the answer'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0ms\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# convert the tuple to string\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "value = ('the answer', 42)\n",
    "s = str(value)  # convert the tuple to string\n",
    "f.write(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "linear-exhibition",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = open('workfile', 'rb+')\n",
    "f.write(b'0123456789abcdef')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "unique-computer",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f.seek(5)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cleared-accommodation",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'5'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f.read(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "random-weather",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " f.seek(-3, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "patent-nothing",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'[1, \"simple\", \"list\"]'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import json\n",
    "json.dumps([1, 'simple', 'list'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "everyday-wages",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "a bytes-like object is required, not 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-38-83ec06b0df75>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\json\\__init__.py\u001b[0m in \u001b[0;36mdump\u001b[1;34m(obj, fp, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)\u001b[0m\n\u001b[0;32m    178\u001b[0m     \u001b[1;31m# a debuggability cost\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    179\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mchunk\u001b[0m \u001b[1;32min\u001b[0m \u001b[0miterable\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 180\u001b[1;33m         \u001b[0mfp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchunk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    181\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    182\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: a bytes-like object is required, not 'str'"
     ]
    }
   ],
   "source": [
    "json.dump(x, f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "musical-alert",
   "metadata": {},
   "outputs": [
    {
     "ename": "JSONDecodeError",
     "evalue": "Expecting value: line 1 column 1 (char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-39-bb45846d9f9b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\json\\__init__.py\u001b[0m in \u001b[0;36mload\u001b[1;34m(fp, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[0;32m    291\u001b[0m     \u001b[0mkwarg\u001b[0m\u001b[1;33m;\u001b[0m \u001b[0motherwise\u001b[0m\u001b[0;31m \u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0mJSONDecoder\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m \u001b[1;32mis\u001b[0m \u001b[0mused\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    292\u001b[0m     \"\"\"\n\u001b[1;32m--> 293\u001b[1;33m     return loads(fp.read(),\n\u001b[0m\u001b[0;32m    294\u001b[0m         \u001b[0mcls\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobject_hook\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mobject_hook\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    295\u001b[0m         \u001b[0mparse_float\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparse_float\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparse_int\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparse_int\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\json\\__init__.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[0;32m    344\u001b[0m             \u001b[0mparse_int\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mparse_float\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    345\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[1;32m--> 346\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    347\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    348\u001b[0m         \u001b[0mcls\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mJSONDecoder\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[1;34m(self, s, _w)\u001b[0m\n\u001b[0;32m    335\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    336\u001b[0m         \"\"\"\n\u001b[1;32m--> 337\u001b[1;33m         \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    339\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[1;34m(self, s, idx)\u001b[0m\n\u001b[0;32m    353\u001b[0m             \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscan_once\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    354\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 355\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Expecting value\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    356\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)"
     ]
    }
   ],
   "source": [
    "x = json.load(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "offshore-finnish",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a number:  12\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "...     try:\n",
    "...         x = int(input(\"Please enter a number: \"))\n",
    "...         break\n",
    "...     except ValueError:\n",
    "...         print(\"Oops!  That was no valid number.  Try again...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "stretch-baseline",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B\n",
      "C\n",
      "D\n"
     ]
    }
   ],
   "source": [
    "class B(Exception):\n",
    "    pass\n",
    "\n",
    "class C(B):\n",
    "    pass\n",
    "\n",
    "class D(C):\n",
    "    pass\n",
    "\n",
    "for cls in [B, C, D]:\n",
    "    try:\n",
    "        raise cls()\n",
    "    except D:\n",
    "        print(\"D\")\n",
    "    except C:\n",
    "        print(\"C\")\n",
    "    except B:\n",
    "        print(\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "political-syndicate",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OS error: [Errno 2] No such file or directory: 'myfile.txt'\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "try:\n",
    "    f = open('myfile.txt')\n",
    "    s = f.readline()\n",
    "    i = int(s.strip())\n",
    "except OSError as err:\n",
    "    print(\"OS error: {0}\".format(err))\n",
    "except ValueError:\n",
    "    print(\"Could not convert data to an integer.\")\n",
    "except:\n",
    "    print(\"Unexpected error:\", sys.exc_info()[0])\n",
    "    raise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "bizarre-church",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cannot open -f\n",
      "C:\\Users\\19498\\AppData\\Roaming\\jupyter\\runtime\\kernel-5a89f570-5f58-4757-b467-5d39b91c01ba.json has 12 lines\n"
     ]
    }
   ],
   "source": [
    "for arg in sys.argv[1:]:\n",
    "    try:\n",
    "        f = open(arg, 'r')\n",
    "    except OSError:\n",
    "        print('cannot open', arg)\n",
    "    else:\n",
    "        print(arg, 'has', len(f.readlines()), 'lines')\n",
    "        f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "romantic-oakland",
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
