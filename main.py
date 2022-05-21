import time

from database import DatabaseManager
from search_tool import SearchTool
from params import params_list_22_5_01_34_is_done

db = DatabaseManager.init()
people_nvidia_collection = db["people-nvidia"]

print("connected to database")
list_of_params = params_list_22_5_01_34_is_done
len_of_params = len(list_of_params)
counter = 1
starting_point = 0
for param in list_of_params:
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
