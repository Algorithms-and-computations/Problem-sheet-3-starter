import random, pylab
N = 5
pos = []
for stat in range(1000):
   posit = set(range(N))
   for t in range(1000000):
      posit = set([min(max(b + random.randint(-1, 1), 0), N - 1) for b in posit])
      if len(posit) == 1: break
   pos.append(posit.pop())
pylab.title('Forward coupling: 1-d diffusion: position of the coupled config.')
pylab.hist(pos, bins=N, range=(-0.5, N - 0.5), density=True)
pylab.savefig('ForwardCoupling.jpg')
pylab.show()

