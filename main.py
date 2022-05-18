import time

from database import DatabaseManager
from search_tool import SearchTool
from params import params_list_18_5_13_32

db = DatabaseManager.init()
people_nvidia_collection = db["people-nvidia"]

print("connected to database")
len_of_params = len(params_list_18_5_13_32)
counter = 1
starting_point = 0
for param in params_list_18_5_13_32:
    if counter <= starting_point:
        print(f"skipping param {counter} / {len_of_params}")
        counter += 1
        continue
    print(f"searching using param {counter} / {len_of_params}")
    result = SearchTool.get_second_to_100_page_result(param)
    print(f"got result for param {counter} / {len_of_params}")
    DatabaseManager.insert_many_if_duplicate_pass(people_nvidia_collection, result)
    counter += 1
    time.sleep(5)

print("finished all the searches.")
