from splitio import get_factory


class SplitClient:
    def __init__(self):
        self.__factory = None
        self.__client = None
        self.__client_installed = False

    @property
    def status(self):
        return self.__client_installed

    def init_client(self, split_sdk_key):
        self.__factory = get_factory(
            split_sdk_key,
            config={
                'featuresRefreshRate': 5,
                'segmentsRefreshRate': 60,
                'metricsRefreshRate': 60,
                'impressionsRefreshRate': 60,
                'ready': 0,
                'connectionTimeout': 3000,
                'readTimeout': 3000,
                'labelsEnabled': True
            }
        )
        self.__factory.block_until_ready(10)
        self.__client = self.__factory.client()
        self.__client_installed = True

    def get_treatment(self, split_name):
        return self.__client.get_treatment('key', split_name)
