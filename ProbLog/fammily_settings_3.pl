base(parent(person,person)).
modes(parent('-','-')).
base(male(person)).
modes(male('+')).
base(female(person)).
modes(female('+')).
base(mother(person,person)).
base(grandmother(person,person)).
base(father(person,person)).
base(male_ancestor(person,person)).
base(female_ancestor(person,person)).

learn(grandmother(person,person)).