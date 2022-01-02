from sys import path
ad = "C:/Users/hp 650 G3/Documents/GitHub/PI"
# ad =
path.append(ad)

from Task02 import *
from Task03 import *
from Task04 import *
import matplotlib.pyplot as plt

def test(rand_inst,prop):
    r = 0.8
    R = 1.2
    n = len(prop)
    res = mate2(rand_inst[0], rand_inst[1])
    ret = []
    for s in [0, 1]:
        cpt = [0] * n
        Ns = len(res[s])
        for elt in res[s]:
            cpt[rand_inst[1][elt].grp] += 1
        for i in range(n):
            if (cpt[i] - 1) / Ns < r or (cpt[i] + 1) / Ns > R:
                ret.append(False)
        ret.append(True)
    return ret


# ### Test instance 2:

# In[26]:


prop2 = [0.9, 0.1]


# In[27]:


def printAnalyse6_2(n):

    N = 200

    for _ in range(N):
        rand_inst = rand_instance2(n)
        fair_rank(rand_inst[0][0].prefer, prop2)
        fair_rank(rand_inst[0][1].prefer, prop2)
    boolean = test(rand_inst, prop2)
    print(n, ":")
    print("s1 verifies the 4/5 - rule ", boolean[0])
    print("s2 verifies the 4/5 - rule ", boolean[1])
    print("________________")


# In[28]:


printAnalyse6_2(1000)
printAnalyse6_2(2000)
printAnalyse6_2(3000)


# ##### Remark:
#
# The schools do not satistfy rigourously the 4/5-rule because there are not enough candidates.

# ### Test instance 3:

# In[29]:


prop3 = [0.5, 0.3, 0.15, 0.05]


# In[30]:


def printAnalyse6_3(n):

    N = 200

    for _ in range(N):
        rand_inst = rand_instance3(n)
        fair_rank(rand_inst[0][0].prefer, prop3)
        fair_rank(rand_inst[0][1].prefer, prop3)
    boolean = test(rand_inst, prop3)
    print(n, ":")
    print("s1 verifies the 4/5 - rule ", boolean[0])
    print("s1 verifies the 4/5 - rule ", boolean[1])
    print("________________")




printAnalyse6_3(1000)
printAnalyse6_3(2000)
printAnalyse6_3(3000)