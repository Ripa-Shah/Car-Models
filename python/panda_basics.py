{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "concerned-worship",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ecological-exception",
   "metadata": {},
   "outputs": [],
   "source": [
    "s=pd.Series(np.random.randn(5),index=[\"a\",\"b\",\"c\",\"d\",\"e\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fewer-report",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a   -0.962516\n",
       "b   -0.544223\n",
       "c   -0.405608\n",
       "d    0.166199\n",
       "e    1.541493\n",
       "dtype: float64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "opened-monkey",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['a', 'b', 'c', 'd', 'e'], dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "corporate-camcorder",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0   -0.569636\n",
       "1   -0.466813\n",
       "2    1.480564\n",
       "3    1.369779\n",
       "4   -0.622535\n",
       "dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(np.random.randn(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "impossible-council",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {\"b\": 1, \"a\": 0, \"c\": 2}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "express-virus",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b    1\n",
       "a    0\n",
       "c    2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "authentic-bangladesh",
   "metadata": {},
   "outputs": [],
   "source": [
    " d = {\"a\": 0.0, \"b\": 1.0, \"c\": 2.0}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "developing-silicon",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    0.0\n",
       "b    1.0\n",
       "c    2.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "annoying-accordance",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b    1.0\n",
       "c    2.0\n",
       "d    NaN\n",
       "a    0.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(d, index=[\"b\", \"c\", \"d\", \"a\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "parental-nickname",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    5\n",
       "b    5\n",
       "c    5\n",
       "d    5\n",
       "e    5\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(5,index=[\"a\",\"b\",\"c\",\"d\",\"e\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "preceding-guyana",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.9625162666756671"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "automatic-recipe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a   -0.962516\n",
       "b   -0.544223\n",
       "c   -0.405608\n",
       "dtype: float64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "careful-combination",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "d    0.166199\n",
       "e    1.541493\n",
       "dtype: float64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[s>s.median()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "increased-iraqi",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "e    1.541493\n",
       "d    0.166199\n",
       "b   -0.544223\n",
       "dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[[4,3,1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "lucky-australian",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    0.381931\n",
       "b    0.580293\n",
       "c    0.666572\n",
       "d    1.180808\n",
       "e    4.671562\n",
       "dtype: float64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.exp(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "pleased-hospital",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "lesbian-strand",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<PandasArray>\n",
       "[ -0.9625162666756671,  -0.5442229818392897, -0.40560751830012304,\n",
       "   0.1661988790204843,   1.5414934821133706]\n",
       "Length: 5, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "seeing-academy",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.96251627, -0.54422298, -0.40560752,  0.16619888,  1.54149348])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.to_numpy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "oriented-demand",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.9625162666756671"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[\"a\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "strong-reality",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.5414934821133706"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[\"e\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "accurate-wrist",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a   -0.962516\n",
       "b   -0.544223\n",
       "c   -0.405608\n",
       "d    0.166199\n",
       "e    1.541493\n",
       "dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "color-worcester",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"e\" in s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "respiratory-contemporary",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"g\" in s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "impossible-relay",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'f'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m   3079\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3080\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3081\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'f'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-f696b56ad3de>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ms\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"f\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    851\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    852\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mkey_is_scalar\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 853\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    854\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    855\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mis_hashable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m_get_value\u001b[1;34m(self, label, takeable)\u001b[0m\n\u001b[0;32m    959\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    960\u001b[0m         \u001b[1;31m# Similar to Index.get_value, but we do not fall back to positional\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 961\u001b[1;33m         \u001b[0mloc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    962\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_values_for_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mloc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabel\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    963\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\19498\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m   3080\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3081\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3082\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3083\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3084\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mtolerance\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'f'"
     ]
    }
   ],
   "source": [
    "s[\"f\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "artistic-lying",
   "metadata": {},
   "outputs": [],
   "source": [
    "s.get(\"f\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "formed-white",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nan"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.get(\"f\",np.nan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "indian-california",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a   -1.925033\n",
       "b   -1.088446\n",
       "c   -0.811215\n",
       "d    0.332398\n",
       "e    3.082987\n",
       "dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s+s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "convenient-landscape",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a   -1.925033\n",
       "b   -1.088446\n",
       "c   -0.811215\n",
       "d    0.332398\n",
       "e    3.082987\n",
       "dtype: float64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "material-envelope",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    0.381931\n",
       "b    0.580293\n",
       "c    0.666572\n",
       "d    1.180808\n",
       "e    4.671562\n",
       "dtype: float64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.exp(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "private-europe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a         NaN\n",
       "b   -1.088446\n",
       "c   -0.811215\n",
       "d    0.332398\n",
       "e         NaN\n",
       "dtype: float64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[1:]+s[:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "resident-climb",
   "metadata": {},
   "outputs": [],
   "source": [
    "s=pd.Series(np.random.randn(10),name=\"FirstSeries\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "secondary-johns",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'FirstSeries'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "comparative-isolation",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    0.093500\n",
       "1    1.190263\n",
       "2   -1.268708\n",
       "3   -1.010986\n",
       "4    1.223249\n",
       "5    1.229629\n",
       "6    1.538024\n",
       "7    0.858271\n",
       "8    0.879515\n",
       "9   -0.609204\n",
       "Name: FirstSeries, dtype: float64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "stone-island",
   "metadata": {},
   "outputs": [],
   "source": [
    "s2=s.rename(\"Different\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "detailed-rouge",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    0.093500\n",
       "1    1.190263\n",
       "2   -1.268708\n",
       "3   -1.010986\n",
       "4    1.223249\n",
       "5    1.229629\n",
       "6    1.538024\n",
       "7    0.858271\n",
       "8    0.879515\n",
       "9   -0.609204\n",
       "Name: Different, dtype: float64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "finnish-provision",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'one': a    1\n",
       " b    2\n",
       " c    3\n",
       " D    4\n",
       " dtype: int64,\n",
       " 'two': a    2\n",
       " b    3\n",
       " c    4\n",
       " d    2\n",
       " e    3\n",
       " f    1\n",
       " dtype: int64}"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d={\"one\": pd.Series([1,2,3,4],index=[\"a\",\"b\",\"c\",\"D\"]),\n",
    "  \"two\":pd.Series([2,3,4,2,3,1], index=[\"a\",\"b\",\"c\",\"d\",\"e\",\"f\"])}\n",
    "d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "documentary-roberts",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "enormous-eagle",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>e</th>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>f</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "D  4.0  NaN\n",
       "a  1.0  2.0\n",
       "b  2.0  3.0\n",
       "c  3.0  4.0\n",
       "d  NaN  2.0\n",
       "e  NaN  3.0\n",
       "f  NaN  1.0"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "concerned-triumph",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>2.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "d  NaN    2\n",
       "b  2.0    3\n",
       "a  1.0    2"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(d, index=[\"d\", \"b\", \"a\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "buried-combat",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>two</th>\n",
       "      <th>three</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>3</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   two three\n",
       "d    2   NaN\n",
       "b    3   NaN\n",
       "a    2   NaN"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(d, index=[\"d\", \"b\", \"a\"], columns=[\"two\", \"three\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "tight-contract",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'one': a    1\n",
       " b    2\n",
       " c    3\n",
       " D    4\n",
       " dtype: int64,\n",
       " 'two': a    2\n",
       " b    3\n",
       " c    4\n",
       " d    2\n",
       " e    3\n",
       " f    1\n",
       " dtype: int64}"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "composite-chapter",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['D', 'a', 'b', 'c', 'd', 'e', 'f'], dtype='object')"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "brazilian-concentration",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['one', 'two'], dtype='object')"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "aquatic-simple",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {\"one\": [1.0, 2.0, 3.0, 4.0], \"two\": [4.0, 3.0, 2.0, 1.0]}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "bound-ivory",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "0  1.0  4.0\n",
       "1  2.0  3.0\n",
       "2  3.0  2.0\n",
       "3  4.0  1.0"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " pd.DataFrame(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "unable-florence",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "a  1.0  4.0\n",
       "b  2.0  3.0\n",
       "c  3.0  2.0\n",
       "d  4.0  1.0"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(d, index=[\"a\", \"b\", \"c\", \"d\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "detailed-spectrum",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = np.zeros((2,), dtype=[(\"A\", \"i4\"), (\"B\", \"f4\"), (\"C\", \"a10\")])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "entertaining-insertion",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([(0, 0., b''), (0, 0., b'')],\n",
       "      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "french-stewart",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[:] = [(1, 2.0, \"Hello\"), (2, 3.0, \"World\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "educated-inspection",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([(1, 2., b'Hello'), (2, 3., b'World')],\n",
       "      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "correct-record",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([(1, 2., b'Hello'), (2, 3., b'World')],\n",
       "      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(data,index=[\"one\",\"two\"])\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "visible-campaign",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>a</th>\n",
       "      <th>b</th>\n",
       "      <th>c</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [a, b, c]\n",
       "Index: []"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(data, columns=[\"a\",\"b\",\"c\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "friendly-psychology",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([(1, 2., b'Hello'), (2, 3., b'World')],\n",
       "      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "biblical-scotland",
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
