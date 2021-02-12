# -*- coding: utf-8 -*-

import numpy as np

# *********** PARAMETER VALUES
# grids
da1 = 40                         # no of asset levels for grid 1
da2 = 220                        # no of asset levels for grid 2
da = da1 + da2                   # no of asset levels
mina = 0.0                      # minimum asset level
maxa = 1700                     # maximum asset level
dr = 2                       # no of entrepr. ability realizations
dy = 5                           # no of income realizations
dk=da                            # levels of capital
mink = 0.05                      # minimum investment level
maxk=maxa                        # maximum investment level


# preferences and technology
bet = 0.867
gam = 1.5
delt = 0.06      # capital depreciation
eta = 1.0         # altruism toward children
ni  = 0.88        # decreasing returns
alph = 0.33      # capital share in non-entrepreneurial sector
abig = 1.0           # constant in nonentrepreneurial production function
pyou = 0.9778     # probability of staying young
pold = 0.911      # probability of staying old (not dying)
replrate = 0.4           # replacement rate for pensions
tauc = 0.0        # consumption tax
taua = 0.0        # capital income tax

indtaua=0         # 0 if taua=0, 1 if taua>0
# taue = 0.20
tauls = 0.0       # lump sum tax
exem=500          # estate taxes exemption level
taub = 0.0        # tax rate on estates
gfrac = 0.0       # frac gov exp/gdp
debtfrac=0.10     # frac gov debt /total capital

# enforcement
eff = 0.75       # prop k when defaulting
# transition matrix nonzero elements
nyoung=dr*dy*da    # possible states for young w or entr
noe = da*dr        # possible states for old entrepreneur
nstates=2*nyoung+noe+da   # states (total)
nonzero=2*(dy*dr+dr+1)*nyoung+(dy*dr+dr+1)*noe+(dy*dr+1)*da
sizeM = 2*nyoung+noe+da # dimension of trans mat M
# number of iter. on iterakhat for which we want to save value functions
nite = 6

# ********* VARIABLES
i = 0
i2 = 0
j = 0
j1 = 0
j2 = 0
jj = 0
l = 0
ll = 0
OpenStatus = 0
imax = 0
indanet = 0
imaxmat = [0,0]
epsi = 0
epsimin = 0
epsinv = 0
epsinvmin = 0
epsir = 0
epsirmin = 0
epsigov = 0
epsigovmin = 0
epsihato = 0   # kohat-newkohat: how bc changes across iter for old
epsihaty = 0   # kohat-newkyhat: how bc changes across iter for young
epsihat = 0    # epsihat=abs((kyhat-newkyhat)+(kohat-newkohat))=0
               # iterate on val funs and bc until it's zero
# equilibrium risk-free interest rate and wages
rbar = 0
rbarmin = 0
rbarmax = 0
rimplied = 0
wage = 0
wageimplied = 0

# pensions
transf = 0

# grids
a = np.zeros(da)