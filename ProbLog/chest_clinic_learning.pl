% Chest Clinic

% Contribution Facts
t(_)::travel.
t(_)::smoker.

% Diseasis
t(_)::tuberculosis :- travel.
t(_)::tuberculosis :- \+ travel.
t(_)::cancer :- smoker.
t(_)::cancer :- \+ smoker.
t(_)::bronchitis :- smoker.
t(_)::bronchitis :- \+ smoker.

% Intermediate
tb_or_ca :- tuberculosis.
tb_or_ca :- cancer.

% Symptons
t(_)::xray_abnormal :- tb_or_ca.
t(_)::xray_abnormal :- \+ tb_or_ca.

t(_)::dyspnea :- tb_or_ca, bronchitis. 
t(_)::dyspnea :- tb_or_ca, \+ bronchitis. 
t(_)::dyspnea :- \+ tb_or_ca, bronchitis. 
t(_)::dyspnea :- \+ tb_or_ca, \+ bronchitis. 