import random
from csv import DictReader


class TermParamSource:
    def __init__(self, track, params, **kwargs):
        # choose a suitable index: if there is only one defined for this track
        # choose that one, but let the user always override index and type.
        if len(track.indices) == 1:
            default_index = track.indices[0].name
            if len(track.indices[0].types) == 1:
                default_type = track.indices[0].types[0].name
            else:
                default_type = None
        else:
            default_index = "reference"
            default_type = None

        # we can eagerly resolve these parameters already in the constructor...
        self._index_name = params.get("index", default_index)
        self._type_name = params.get("type", default_type)
        self._cache = params.get("cache", False)
        # ... but we need to resolve "profession" lazily on each invocation later
        self._params = params
        # Determines whether this parameter source will be "exhausted" at some point or
        # Rally can draw values infinitely from it.
        self.infinite = True

        with open("babynames1880-2020.csv", 'r') as f:
            dict_reader = DictReader(f)
            self.list_of_dict = list(dict_reader)

    def partition(self, partition_index, total_partitions):
        return self

    def params(self):
        # you must provide all parameters that the runner expects
        return {
            "body": {
                "query": {
                    "term": {
                        "name": "%s" % random.choice(self.list_of_dict)["Name"]
                    }
                }
            },
            "index": self._index_name,
            "type": self._type_name,
            "cache": self._cache
        }


def register(registry):
    registry.register_param_source("custom-term-param-source", TermParamSource)