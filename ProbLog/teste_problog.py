# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:00:01 2020

@author: cleiton
"""

from problog.program import PrologString, SimpleProgram
from problog import get_evaluatable
from problog.logic import Constant,Var,Term,AnnotatedDisjunction

p1 = PrologString("""
% Car Diagnosis 0 (Norsys Softwre)
% Implemented by: Cleiton Almeida

0.06::altenator_f.
0.38::battery_age(new); 0.43::battery_age(old); 0.19::battery_age(very_old).
0.06::main_fuse_f.
0.01::distributer_f.
0.01::starter_motor_f.
0.72::spark_plugs(ok); 0.10::spark_plugs(too_wide); 0.18::spark_plugs(fouled).

0.50::charging_system_f :- \+ altenator_f.
0.67::charging_system_f :- altenator_f.

0.93::battery(strong) :- \+ charging_system_f, battery_age(new).
0.05::battery(weak) :- \+ charging_system_f, battery_age(new).
0.02::battery(dead) :- \+ charging_system_f, battery_age(new).

0.80::battery(strong) :- \+ charging_system_f, battery_age(old).
0.15::battery(weak) :- \+ charging_system_f, battery_age(old).
0.05::battery(dead) :- \+ charging_system_f, battery_age(old).

0.57::battery(strong) :- \+ charging_system_f, battery_age(very_old).
0.29::battery(weak) :- \+ charging_system_f, battery_age(very_old).
0.14::batteryt(dead) :- \+charging_system_f, battery_age(very_old).

0.02::battery(strong) :- charging_system_f, battery_age(new).
0.32::battery(weak) :- charging_system_f, battery_age(new).
0.66::battery(dead) :- charging_system_f, battery_age(new).

0.04::battery(strong) :- charging_system_f, battery_age(old).
0.20::battery(weak) :- charging_system_f, battery_age(old).
0.76::battery(dead) :- charging_system_f, battery_age(old).

0.03::battery(strong) :- charging_system_f, battery_age(very_old).
0.04::battery(weak) :- charging_system_f, battery_age(very_old).
0.93::battery(dead) :- charging_system_f, battery_age(very_old).

0.93::headlights(bright) :- battery_volt(strong).
0.01::headlights(dim) :- battery_volt(strong).
0.06::headlights(off) :- battery_volt(strong).

0.02::headlights(bright) :- battery_volt(weak).
0.91::headlights(dim) :- battery_volt(weak).
0.07::headlights(off) :- battery_volt(weak).

0.01::headlights(bright) :- battery_volt(dead).
0.01::headlights(dim) :- battery_volt(dead).
0.98::headlights(off) :- battery_volt(dead).

0.88::voltage_plug(strong) :- \+main_fuse_f, \+distributer_f, battery(strong).
0.08::voltage_plug(weak)   :- \+main_fuse_f, \+distributer_f, battery(strong).
0.04::voltage_plug(none)   :- \+main_fuse_f, \+distributer_f, battery(stron).

0.02::voltage_plug(strong) :- \+main_fuse_f, \+distributer_f, battery(weak).
0.87::voltage_plug(weak)   :- \+main_fuse_f, \+distributer_f, battery(weak).
0.11::voltage_plug(none)   :- \+main_fuse_f, \+distributer_f, battery(weak).

0.01::voltage_plug(strong) :- \+main_fuse_f, \+distributer_f, battery(dead).
0.01::voltage_plug(weak)   :- \+main_fuse_f, \+distributer_f, battery(dead).
0.98::voltage_plug(none)   :- \+main_fuse_f, \+distributer_f, battery(dead).


0.25::voltage_plug(strong) :- \+main_fuse_f, distributer_f, battery(strong).
0.50::voltage_plug(weak)   :- \+main_fuse_f, distributer_f, battery(strong).
0.25::voltage_plug(none)   :- \+main_fuse_f, distributer_f, battery(strong).

0.25::voltage_plug(strong) :- \+main_fuse_f, distributer_f, battery(weak).
0.25::voltage_plug(weak)   :- \+main_fuse_f, distributer_f, battery(weak).
0.50::voltage_plug(none)   :- \+main_fuse_f, distributer_f, battery(weak).

0.33::voltage_plug(strong) :- \+main_fuse_f, distributer_f, battery(dead).
0.33::voltage_plug(weak)   :- \+main_fuse_f, distributer_f, battery(dead).
0.34::voltage_plug(none)   :- \+main_fuse_f, distributer_f, battery(dead).


0.25::voltage_plug(strong) :- main_fuse_f, \+distributer_f, battery(strong).
0.25::voltage_plug(weak)   :- main_fuse_f, \+distributer_f, battery(strong).
0.50::voltage_plug(none)   :- main_fuse_f, \+distributer_f, battery(strong).

0.33::voltage_plug(strong) :- main_fuse_f, \+distributer_f, battery(weak).
0.33::voltage_plug(weak)   :- main_fuse_f, \+distributer_f, battery(weak).
0.33::voltage_plug(none)   :- main_fuse_f, \+distributer_f, battery(weak).

0.33::voltage_plug(strong) :- main_fuse_f, \+distributer_f, battery(dead).
0.33::voltage_plug(weak)   :- main_fuse_f, \+distributer_f, battery(dead).
0.33::voltage_plug(none)   :- main_fuse_f, \+distributer_f, battery(dead).


0.33::voltage_plug(strong) :- main_fuse_f, distributer_f, battery(strong).
0.33::voltage_plug(weak)   :- main_fuse_f, distributer_f, battery(strong).
0.33::voltage_plug(none)   :- main_fuse_f, distributer_f, battery(strong).

0.33::voltage_plug(strong) :- main_fuse_f, distributer_f, battery(weak).
0.33::voltage_plug(weak)   :- main_fuse_f, distributer_f, battery(weak).
0.33::voltage_plug(none)   :- main_fuse_f, distributer_f, battery(weak).

0.33::voltage_plug(strong) :- main_fuse_f, distributer_f, battery(dead).
0.33::voltage_plug(weak)   :- main_fuse_f, distributer_f, battery(dead).
0.33::voltage_plug(none)   :- main_fuse_f, distributer_f, battery(dead).


0.98::spark_qual(good)     :- \+spark_plugs(ok), voltage_plug(strong).
0.01::spark_qual(bad)      :- \+spark_plugs(ok), voltage_plug(strong).
0.01::spark_qual(very_bad) :- \+spark_plugs(ok), voltage_plug(strong).

0.04::spark_qual(good)     :- \+spark_plugs(ok), voltage_plug(weak).
0.92::spark_qual(bad)      :- \+spark_plugs(ok), voltage_plug(weak).
0.04::spark_qual(very_bad) :- \+spark_plugs(ok), voltage_plug(weak).

0.01::spark_qual(good)     :- \+spark_plugs(ok), voltage_plug(none).
0.01::spark_qual(bad)      :- \+spark_plugs(ok), voltage_plug(none).
0.98::spark_qual(very_bad) :- \+spark_plugs(ok), voltage_plug(none).


0.08::spark_qual(good)     :- \+spark_plugs(too_wide), voltage_plug(strong).
0.84::spark_qual(bad)      :- \+spark_plugs(too_wide), voltage_plug(strong).
0.08::spark_qual(very_bad) :- \+spark_plugs(too_wide), voltage_plug(strong).

0.14::spark_qual(good)     :- \+spark_plugs(too_wide), voltage_plug(weak).
0.14::spark_qual(bad)      :- \+spark_plugs(too_wide), voltage_plug(weak).
0.72::spark_qual(very_bad) :- \+spark_plugs(too_wide), voltage_plug(weak).

0.06::spark_qual(good)     :- \+spark_plugs(too_wide), voltage_plug(none).
0.06::spark_qual(bad)      :- \+spark_plugs(too_wide), voltage_plug(none).
0.88::spark_qual(very_bad) :- \+spark_plugs(too_wide), voltage_plug(none).


0.08::spark_qual(good)     :- \+spark_plugs(fouled), voltage_plug(strong).
0.84::spark_qual(bad)      :- \+spark_plugs(fouled), voltage_plug(strong).
0.08::spark_qual(very_bad) :- \+spark_plugs(fouled), voltage_plug(strong).

0.09::spark_qual(good)     :- \+spark_plugs(fouled), voltage_plug(weak).
0.09::spark_qual(bad)      :- \+spark_plugs(fouled), voltage_plug(weak).
0.82::spark_qual(very_bad) :- \+spark_plugs(fouled), voltage_plug(weak).

0.04::spark_qual(good)     :- \+spark_plugs(fouled), voltage_plug(none).
0.04::spark_qual(bad)      :- \+spark_plugs(fouled), voltage_plug(none).
0.92::spark_qual(very_bad) :- \+spark_plugs(fouled), voltage_plug(none).

0.88::spark_timing(good)     :- \+distributer_f.
0.10::spark_timing(bad)      :- \+distributer_f.
0.02::spark_timing(very_bad) :- \+distributer_f.
0.33::spark_timing(good)     :- distributer_f.
0.33::spark_timing(bad)      :- distributer_f.
0.33::spark_timing(very_bad) :- distributer_f.

0.04::starter_sytem_f :- \+main_fuse_f, \+starter_motor_f, battery(strong).
0.15::starter_sytem_f :- \+main_fuse_f, \+starter_motor_f, battery(weak).
0.95::starter_sytem_f :- \+main_fuse_f, \+starter_motor_f, battery(dead).

0.66::starter_sytem_f :- \+main_fuse_f, starter_motor_f, battery(strong).
0.50::starter_sytem_f :- \+main_fuse_f, starter_motor_f, battery(weak).
0.66::starter_sytem :- \+main_fuse_f, starter_motor_f, battery(dead).

0.66::starter_sytem_f :- main_fuse_f, \+starter_motor_f, battery(strong).
0.50::starter_sytem_f :- main_fuse_f, \+starter_motor_f, battery(weak).
0.50::starter_sytem_f :- main_fuse_f, \+starter_motor_f, battery(dead).

0.50::starter_sytem_f :- main_fuse_f, starter_motor_f, battery(strong).
0.50::starter_sytem_f :- main_fuse_f, starter_motor_f, battery(weak).
0.50::starter_sytem_f :- main_fuse_f, starter_motor_f, battery(dead).

0.82:car_cranks :- \+starter_system_f.
0.06:car_cranks :- starter_system_f.

0.78::car_starts :- car_cranks, spark_timing(good), spark_quality(good).
0.40::car_starts :- car_cranks, spark_timing(good), spark_quality(bad).
0.04::car_starts :- car_cranks, spark_timing(good), spark_quality(vary_bad).
0.70::car_starts :- car_cranks, spark_timing(bad), spark_quality(good).
0.63::car_starts :- car_cranks, spark_timing(bad), spark_quality(bad).
0.20::car_starts :- car_cranks, spark_timing(bad), spark_quality(vary_bad).
0.67::car_starts :- car_cranks, spark_timing(very_bad), spark_quality(good).
0.33::car_starts :- car_cranks, spark_timing(very_bad), spark_quality(bad).
0.50::car_starts :- car_cranks, spark_timing(very_bad), spark_quality(vary_bad).

0.08::car_starts :- \+car_cranks, spark_timing(good), spark_quality(good).
0.08::car_starts :- \+car_cranks, spark_timing(good), spark_quality(bad).
0.01::car_starts :- \+car_cranks, spark_timing(good), spark_quality(vary_bad).
0.33::car_starts :- \+car_cranks, spark_timing(bad), spark_quality(good).
0.50::car_starts :- \+car_cranks, spark_timing(bad), spark_quality(bad).
0.10::car_starts :- \+car_cranks, spark_timing(bad), spark_quality(vary_bad).
0.50::car_starts :- \+car_cranks, spark_timing(very_bad), spark_quality(good).
0.50::car_starts :- \+car_cranks, spark_timing(very_bad), spark_quality(bad).
0.33::car_starts :- \+car_cranks, spark_timing(very_bad), spark_quality(vary_bad).

% Inferences
query(altenator_f).
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