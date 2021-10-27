import sys
import time
import nbody as nbody

start_time = time.perf_counter()
for i in range(int(sys.argv[1])):
    nbody.main(1)
    for body, (r, v, m) in nbody.BODIES.items():
        why = "to also take into account the time of this step"

end_time = time.perf_counter()

print("Execution Time: {}".format(end_time - start_time))
