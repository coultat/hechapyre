{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "import urllib\n",
    "import json\n",
    "from store.sample import placements\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = json.loads('{\"website\": \"yieldlove.com\",\"device\": \"_d\",\"placements\":{\"name\": \"yieldlove.com_d_300x250_1\",\"sizes\": [\"320x150\", \"320x50\", \"320x75\", \"320x100\"],\"created\": \"no\",\"id\": \"\"}}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [a]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = json.loads('{\"website\": \"venezuela.com\",\"device\": \"_d\",\"placements\":{\"name\": \"venezuela.com_d_300x250_1\",\"sizes\": [\"320x150\", \"320x50\", \"320x75\", \"320x100\"],\"created\": \"no\",\"id\": \"\"}}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "helper1 = json.dumps(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "helper2 = json.loads(helper1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "placements = ['yieldlove.com_d_300x250_1', 'yieldlove.com_d_970x250_1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def ordering_list(placements):\n",
    "    data = {}\n",
    "    final = []\n",
    "    placements.sort()\n",
    "    for placement in placements:\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = [b]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "a.extend(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'website': 'yieldlove.com',\n",
       "  'device': '_d',\n",
       "  'placements': {'name': 'yieldlove.com_d_300x250_1',\n",
       "   'sizes': ['320x150', '320x50', '320x75', '320x100'],\n",
       "   'created': 'no',\n",
       "   'id': ''}},\n",
       " {'website': 'venezuela.com',\n",
       "  'device': '_d',\n",
       "  'placements': {'name': 'venezuela.com_d_300x250_1',\n",
       "   'sizes': ['320x150', '320x50', '320x75', '320x100'],\n",
       "   'created': 'no',\n",
       "   'id': ''}}]"
      ]
     },
     "execution_count": 93,
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
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['venezuela.com']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[result['website'] for result in a if 'venezuela.com' in result['website']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
