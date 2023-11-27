import sys
import time
import multiprocessing as mp
from pathlib import Path
from multiprocessing.pool import ThreadPool
from threading import Thread
from typing import Callable
import statistics

import psutil
import requests


def control_group() -> None:
    time.sleep(5)


# def webtoonscraper() -> None:
#     from WebtoonScraper.scrapers import BestChallengeScraper
#     scraper = BestChallengeScraper(816046)
#     scraper.download_webtoon()


def download_image(i) -> None:
    try:
        # Random image from Wikipedia.
        res = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/"
                           "Chrysler_Building_Midtown_Manhattan_New_York_City_1932.jpg/"
                           "1920px-Chrysler_Building_Midtown_Manhattan_New_York_City_1932.jpg")
    except requests.ConnectionError:
        print("download failed.")
        return
    Path(f"test_images/{i:05d}.png").write_bytes(res.content)


def threadpool() -> None:
    with ThreadPool(30) as p:
        p.map(download_image, range(1000))


def threading_thread() -> None:
    for i in range(0, 1000, 50):
        threads = [Thread(target=download_image, args=(j,)) for j in range(i, i + 50)]

        # Using list comprehension is more performent.
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        # for thread in threads:
        #     thread.start()
        # for thread in threads:
        #     thread.join()


def monitor(target) -> tuple[list[float], list[float], list[int], float]:
    # The code is from https://stackoverflow.com/a/2468983/21997874, with some modifies.
    worker_process = mp.Process(target=target)
    worker_process.start()
    p = psutil.Process(worker_process.pid)

    received_bytes_old = psutil.net_io_counters().bytes_recv
    start = time.perf_counter()
    cpu_percents_in_total: list[float] = []
    cpu_percents: list[float] = []
    received_bytes_list: list[int] = []
    try:
        while worker_process.is_alive():
            cpu_percents_in_total.append(psutil.cpu_percent())
            cpu_percents.append(p.cpu_percent())

            received_bytes_new = psutil.net_io_counters().bytes_recv
            received_bytes_list.append(received_bytes_new - received_bytes_old)
            received_bytes_old = received_bytes_new

            time.sleep(0.1)
    finally:
        worker_process.join()
        return cpu_percents_in_total, cpu_percents, received_bytes_list, time.perf_counter() - start


def summarize(name: str, values: list[int] | list[float]) -> None:
    print(f"Summary for {name}:")
    print(f"    Stdev:  {statistics.stdev(values)}")
    print(f"    Mean:   {statistics.mean(values)}")
    print(f"    Median: {statistics.median(values)}")
    print(f"    Max:    {max(values)}")
    print(f"    Min:    {min(values)}")


def report_performance(target_function: Callable) -> None:
    cpu_percents_in_total, cpu_percents, received_bytes_list, elapsed_time = monitor(target=target_function)
    print(f"Target: {target_function.__name__}\n")
    print(f"Elapsed time: {elapsed_time}\n")
    print(sys.version)
    print()
    print("| CPU Percent in Total | CPU Percent | Received Bytes Per 0.1sec |")
    print("|----------------------|-------------|---------------------------|")
    for cpu_percent_in_total, cpu_percent, memory_info in zip(cpu_percents_in_total, cpu_percents, received_bytes_list):
        print(f"| {int(cpu_percent_in_total): 19d}% | {int(cpu_percent): 10d}% | {memory_info: 25d} |")
    print()

    print("```")
    summarize("cpu_percents_in_total", cpu_percents_in_total)
    summarize("cpu_percents", cpu_percents)
    summarize("received_bytes_list", received_bytes_list)
    print("```")


if __name__ == '__main__':
    report_performance(control_group)
    # report_performance(threadpool)
    # report_performance(threading_thread)
