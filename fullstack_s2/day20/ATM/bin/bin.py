#__author:  "Jing Xu"
#date:  2018/1/23

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from module import main

main.main()