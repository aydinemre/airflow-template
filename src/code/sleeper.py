# -*- coding: utf-8 -*-

# Created by emre.aydin (eaydin@boynergrup.com) at 2019-09-02
import time


class Sleeper:
    def __init__(self, sleep_time=5):
        self.sleep_time = sleep_time

    def run(self):
        time.sleep(self.sleep_time)


def main(sleep_time=10):

    sleeper = Sleeper(sleep_time)
    sleeper.run()
