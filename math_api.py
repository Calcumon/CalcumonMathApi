import random

def gen_eqns(int_range, num_params, step = 1):
  parameters = []
  for _ in range(0, num_params):
    parameters.append(random.randint(1, int_range))
  indx = 0
  while indx < len(parameters):
    ans = parameters[indx] + parameters[indx + step]
    eqn_str = str(parameters[indx]) + ' + ' + str(parameters[indx + 1])
    indx += step + 1
  return eqn_str, ans

def choose_phase(phase):
  eqns = []
  if phase == 1:
    for _ in range(9):
      eqns.append(gen_eqns(10, 2))
  # if phase == 2:
  #   eqn = gen_eqn(20, 2)
  # if phase == 3:
  #   eqn = gen_eqn(20, 2)
  return eqns

def gen_guesses(start, end, num, ans): 
    res = []
    while len(res) < num:
        guess = random.randint(start, end)
        if guess not in res and guess != ans:
          res.append(guess)
    return res


# print(choose_phase())