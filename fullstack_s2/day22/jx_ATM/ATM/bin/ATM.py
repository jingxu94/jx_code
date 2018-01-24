#__author:  "Jing Xu"
#date:  2018/1/24

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == "__main__":
	main.run()
