import requests


class ApiRequest:

    def __init__(self,  base_url, end_point, request_method="GET", api_key=None, headers=None):
        self._api_key = api_key
        self._base_url = base_url
        self._end_point = end_point
        self._request_method = request_method
        self._headers = headers
        # {'Content-type': 'application/json', 'API_KEY': self._api_key}

    def __call__(self):
        if self._base_url[-1] != "/":
            self._base_url = self._base_url + "/"

        url = self._base_url + self._end_point
        self.req = requests.request(self._request_method, url)
        if self.req.status_code != 200:
            return self.req.status_code
        print(self.req.status_code)
        return self.req

    def data_response(self):
        """
        returns json data from an api call
        :return: json
        """
        return self.req.json()

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, new_api_key: str):
        self._api_key = new_api_key

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, new_base_url):
        self._base_url = new_base_url

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, new_end_point):
        self._end_point = new_end_point

    @property
    def request_method(self):
        return self._request_method

    @request_method.setter
    def request_method(self, new_request_method):
        self._request_method = new_request_method

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, new_headers: dict):
        """
        method that creates a new header for request
        :param new_headers: dict
        """
        self._headers = new_headers


