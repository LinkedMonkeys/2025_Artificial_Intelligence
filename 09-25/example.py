from logic import *

b = Symbol('badge')
t = Symbol('ticket')
e = Symbol('entry')
r = Symbol('registration desk')

A = Biconditional(e, And(b, t))
B = Implication(e, r)
C = Implication(Not(r), Not(b))

knowledge_base = And(A, B, C)

goal = Implication(t, r)
goal2 = Implication(And(b, t), r)

print(model_check(knowledge_base, goal))
print(model_check(knowledge_base, goal2))