import random

def gen_eqns(int_range, num_params, step = 1):
  parameters = []
  eqn = {}
  for _ in range(0, num_params):
    parameters.append(random.randint(1, int_range))
  indx = 0
  while indx < len(parameters):
    ans = parameters[indx] + parameters[indx + step]
    eqn_str = str(parameters[indx]) + '+' + str(parameters[indx + 1])
    eqn[eqn_str] = str(ans)
    indx += step + 1
  return eqn

def choose_phase():
  eqns = {}
  for _ in range(0, 6):
    eqns.update(gen_eqns(10, 2))
  for _ in range(0, 6):
    eqns.update(gen_eqns(20, 2))
  for _ in range(0, 6):
    eqns.update(gen_eqns(20, 2))
  return eqns


print(choose_phase())