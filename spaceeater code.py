{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.rename(r'C:/Users/user/Desktop/DATA/new.txt',r'C:/Users/user/Desktop/DATA/new.py')\n",
    "filename1 = 'new.py'\n",
    "fileA = open(filename1, 'w')\n",
    "a='''import os\n",
    "\n",
    "filename1 = 'p.txt'\n",
    "fileA = open(filename1, 'r')\n",
    "filename2 = 'k.txt'\n",
    "fileB = open(filename2, 'a')\n",
    "data = fileA.read()\n",
    "fileB.write(data)\n",
    "for i in range(10):\n",
    "        fileB.write(data)\n",
    "fileA.close();\n",
    "fileB.close();\n",
    "os.remove(\"p.txt\")\n",
    "os.rename(\"k.txt\" , \"p.txt\")'''\n",
    "\n",
    "fileA.write(a)\n",
    "fileA.close();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Traceback (most recent call last):\\n  File \"C:\\\\Users\\\\user\\\\Desktop\\\\DATA\\\\new.py\", line 7, in <module>\\n    data = fileA.read()\\nMemoryError'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import subprocess\n",
    "subprocess.getoutput(\"new.py\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
