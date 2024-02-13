import random, pylab
N = 5
pos = []
for statistic in range(100000):
   all_arrows = {}
   time_tot = 0
   while True:
      time_tot -= 1
      old_pos = set(range(0, N))
      arrows = [random.randint(-1, 1) for i in range(N)]
      if arrows[0] == -1: arrows[0] = 0
      if arrows[N - 1] == 1: arrows[N - 1] = 0
      all_arrows[time_tot] = arrows
      positions = set(range(N))
      for t in range(time_tot, 0):
         positions = set([b + all_arrows[t][b] for b in positions])
      if len(positions) == 1: break
   a=positions.pop()
   pos.append(a)
pylab.title('Backward coupling: 1-d with walls: position at t=0')
pylab.hist(pos, bins=N, range=(-0.5, N - 0.5), density=True)
pylab.savefig('backward_position_t0.png')
pylab.show()
