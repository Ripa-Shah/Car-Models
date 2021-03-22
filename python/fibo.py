{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "possible-trinidad",
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
   "execution_count": 5,
   "id": "communist-stewart",
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
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fib(7)\n",
    "fib2(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "continuous-branch",
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
