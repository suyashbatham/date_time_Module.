# import time
# import random
# # from time import perf_counter as my_timer
# # from time import monotonic as my_timer
# from time import process_time as my_timer
# input("press enter to start")
# wait_timer = random.randint(1,6)
# time.sleep(wait_timer)
# start_time = my_timer()
# input("press enter to stop")
# end_time = my_timer()
# print("Started at"+time.strftime("%X",time.localtime(start_time)))
# print("Ended at"+time.strftime("%x",time.localtime(end_time)))
# print("duration{}".format(start_time-end_time))

import time
print("time():\t\t\t",time.get_clock_info('time'))
print("process_time():\t",time.get_clock_info('process_time'))
print("monotonic:\t",time.get_clock_info('monotonic'))
print("perf_couner():\t",time.get_clock_info('perf_counter'))