import json
import time

import redis
from django.core.management.base import CommandError, BaseCommand


# noinspection PyMethodMayBeStatic
class Command(BaseCommand):
    def _get_message_from_edge(self) -> dict:
        """
        Returns data from super complex undocumented system. Consider it
        non mutable (you can rename it, move it, but don't change the contents).
        :return: json converted to dictionary
        """
        yield json.load(open("example.json"))

    def _store_message_in_database(self, timestamp: str, message: str) -> bool:
        """
        Stores given CSV string in proprietary database. Consider it non mutable
        (you can rename it, move it, but don't change the contents).
        :param timestamp: Datetime in format: "2020-01-21T09:32:34" as string
        :param message: CSV represented as string
        :return: boolean result of the call
        """
        time.sleep(0.5)
        r = redis.Redis()
        r.set(timestamp, message)

    def handle(self, *args, **options):
        for message in self._get_message_from_edge():
            values = message["Values"]
            csv_message = "{FACTORY},{ZONE},{CELL},{MACHINE_GROUP}," \
                          "{MACHINE},{MACHINE_ID}".format(**values)
            self._store_message_in_database(values["TIMESTAMP"], csv_message)
