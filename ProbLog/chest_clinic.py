# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:00:01 2020

@author: cleiton
"""

from problog.program import PrologString, SimpleProgram
from problog import get_evaluatable, lfi
from problog.logic import Constant,Var,Term,AnnotatedDisjunction

p1 = PrologString("""
% Chest Clinic

% Contribution Facts
0.01::travel.
0.50::smoker.

% Diseasis
0.05::tuberculosis :- travel.
0.01::tuberculosis :- \+ travel.
0.10::cancer :- smoker.
0.01::cancer :- \+ smoker.
0.60::bronchitis :- smoker.
0.30::bronchitis :- \+ smoker.

% Intermediate
tb_or_ca :- tuberculosis.
tb_or_ca :- cancer.

% Symptons
0.98::xray_abnormal :- tb_or_ca.
0.05::xray_abnormal :- \+ tb_or_ca.

0.90::dyspnea :- tb_or_ca, bronchitis. 
0.70::dyspnea :- tb_or_ca, \+ bronchitis. 
0.80::dyspnea :- \+ tb_or_ca, bronchitis. 
0.10::dyspnea :- \+ tb_or_ca, \+ bronchitis. 

% Findings
evidence(dyspnea).
evidence(smoker).
evidence(xray_abnormal).
evidence(\+travel).

% Inferences
query(tuberculosis).
query(cancer).
query(tb_or_ca).
query(bronchitis).
query(xray_abnormal).
query(dyspnea).
""")

coin,heads,tails,win,query = Term('coin'),Term('heads'),Term('tails'),Term('win'),Term('query')
C = Var('C')
p = SimpleProgram()
p += coin(Constant('c1'))
p += coin(Constant('c2'))
p 
p += AnnotatedDisjunction([heads(C,p=0.4), tails(C,p=0.6)], coin(C))
p += (win << heads(C))
p += query(win)


print(get_evaluatable().create_from(p1).evaluate())