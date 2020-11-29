import requests


class Endpoints:
    INFO = '/info'
    BEAR = '/bear'
    BEAR_WITH_ID = '/bear/'


class AlaskaCRUD:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8091/"

    #region GET

    def get_info(self):
        return requests.get(self.base_url + Endpoints.INFO)

    def get_all_bears(self):
        return requests.get(self.base_url + Endpoints.BEAR)

    def get_bear_by_id(self, bear_id):
        return requests.get(self.base_url + Endpoints.BEAR_WITH_ID + str(bear_id))

    #endregion

    #region POST

    def create_bear(self, data):
        return requests.post(self.base_url + Endpoints.BEAR, json=data)

    #endregion

    #region PUT

    def update_bear(self, bear_id, data):
        return requests.put(self.base_url + Endpoints.BEAR_WITH_ID + str(bear_id), json=data)

    #endregion

    #region DELETE

    def delete_all_bears(self):
        return requests.delete(self.base_url + Endpoints.BEAR)

    def delete_bear_by_id(self, bear_id):
        return requests.delete(self.base_url + Endpoints.BEAR_WITH_ID + str(bear_id))

    #endregion
