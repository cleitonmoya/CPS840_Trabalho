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
evidence(travel).

% Inferences
query(tuberculosis).
query(cancer).
query(tb_or_ca).
query(bronchitis).
query(xray_abnormal).
query(dyspnea).