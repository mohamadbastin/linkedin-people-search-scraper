class SearchParser:

    @staticmethod
    def parse_profile_links_search_result(response):
        result = (response[len(response) // 2:])
        list_of_employees_links = set()
        tmp_list = []
        sample = "https://www.linkedin.com/in/"
        c = 1
        for i in range(len(result) - 28):
            if sample in result[i:i + 28]:
                tmp_list.append(result[i:i + 1000].split("&")[0])
                c += 1

        for i in tmp_list:
            if "ACoAA" not in i:
                list_of_employees_links.add(i)

        return list_of_employees_links

    @staticmethod
    def create_dictionaries_from_links(loel):
        final_list = []
        for i in loel:
            final_list.append({
                "profile_link": str(i)
            })
        return final_list
