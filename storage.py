import redis
import settings
import json


class Store:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL)

    def set_items(self, key, items, number):
        json_object = json.dumps(items)
        self.redis.set(key, json_object)

    def get_item(self, key):
        unpacked = json.loads(self.redis.get(key))
        return unpacked

    def already_exist(self, key):
        return self.redis.exists(key)

    def reset_data(self):
        self.redis.flushall()
