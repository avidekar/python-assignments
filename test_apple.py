# # Time 	Door Status
# # 11:20	A	Open
# # 11:30	B	Close
# # 11:50	A	Close
# # 1:01	C	Open
# # 1:07	A	Open
# # 1:15	D	Close
# # 1:50	B	Close
# # 2:30	A	Open
# # 3:00	C	Open
# # 4:00	A	Close
# # 5:50	B	Close
# # 8:10	A	Open
#
# # A -> 11:20 - 11:50; 1:07 - 4:00 (30 mins + 173 mins) = 203mins/2 = 101.5
# import csv
# door_status = {'A' : ["11:20"], }
# door_average_time = {'A' : [30]} # minutes
#
# # dictionary to implies to entries for all the doors that were open
# # key is door name, value is the start time for the door to open
# door_status = {}
#
# # dictionary that implies each door name as key and the time for the door to remain open as a
# # list in value
# door_average_time = {}
#
# def get_average_door_time(path_to_file):
#
#     with open(path_to_file, "r") as file_obj:
#         csv_parser = csv.DictReader(file_obj)
#         for row in csv_parser:
#             if (row['Status'] == 'Close'):
#                 if (row['Door'] not in door_status):
#                     continue
#                 else:
#                     time_diff = door_status[row['Door']] - row['Time']
#                     del door_status[row['Door']]
#                     if row['Door'] in door_average_time:
#                         door_average_time[row['Door']].append(time_diff)
#                     else:
#                         door_average_time[row['Door']] = [time_diff]
#
#             else: # if row['Status'] == Open:
#                 if row['Door'] in door_status:
#                     continue
#                 else:
#                     door_status[row['Door']] = row['Time']
#
#
# # door_average_time - example :-
#         # door_average_time = {'A' : [30, 10, 40],
# #                              'B' : [10, 50, 20],
# #                              'C' : [60, 110]
# #                             }
#
#
# for door_name, time_delta in door_average_time.items():
#     avg_time = sum(time_delta) / len(time_delta)
#     print(" Door : {} ; Average Time : {}".format(door_name, avg_time))
#
#
#
#         if status == 'Close':
#             if door in door_status:
#                 time_door_open = time_close - door_status[door]
#                 del door_status[door]
#
#
#



# def f(x, l=[]):
#     l = []
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# # l = [1,2,3,4,5]
#
# # f(7, l)
#
# f(2)
# f(3, [1,2,3])
# f(4)
#

#A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) # {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
# A1 = range(10) # [0,1,2,3,4,5,6,7,8,9] - or - iterator object
# A2 = sorted([i for i in A1 if i in A0]) # []
# A3 = sorted([A0[s] for s in A0]) # [1,2,3,4,5]
# A4 = [i for i in A1 if i in A3] # [1,2,3,4,5]
# A5 = {i:i*i for i in A1} # {0 : 0, 1: 1, 2: 4, 3: 9, 4: 16, ...}
# A6 = [[i,i*i] for i in A1] # [[0,0], [1,1], [2,4], [3,9].. ]
#
