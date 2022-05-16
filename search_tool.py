import requests

from config import headers, cookies
from search_parser import SearchParser


class SearchTool:

    @staticmethod
    def _clear_params(params: dict):
        try:
            del params['sid']
        except KeyError:
            pass
        return params

    @staticmethod
    def get_first_page_result(params):
        params = SearchTool._clear_params(params)
        response = requests.get('https://www.linkedin.com/search/results/people/', params=params, cookies=cookies,
                                headers=headers)

        return SearchParser.parse_profile_links_search_result(response.text)

    @staticmethod
    def get_second_to_100_page_result(params):
        params = SearchTool._clear_params(params)
        params['page'] = '2'
        result = set()
        for i in range(2, 101):
            params['page'] = str(i)
            response = requests.get('https://www.linkedin.com/search/results/people/', params=params, cookies=cookies,
                                    headers=headers)
            tmp_set = SearchParser.parse_profile_links_search_result(response.text)
            for link in tmp_set:
                result.add(link)
            print(f"got page {i}'s result...")

        return result
