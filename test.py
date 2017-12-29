#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import pandas as pd
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

df = pd.read_csv('csvdata/issues.csv',index_col=1,encoding="gb18030")
df.loc[(df['状态'] == "新建")&(df["作者"]=="吴祎楠")["作者","#","状态","主题"]]