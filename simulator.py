import threading
import time
import random

class CacheLine:
    def __init__(self):
        self.state = 'I'  # I (Invalid), S (Shared), M (Modified)
        self.data = None

class Cache:
    def __init__(self, processor_id):
        self.processor_id = processor_id
        self.cache = {}
        self.lock = threading.Lock()

    def read(self, address, memory, cache_list, use_coherence):
        with self.lock:
            if address in self.cache and self.cache[address].state != 'I':
                print(f"[P{self.processor_id}] READ hit {address}, state: {self.cache[address].state}")
                return self.cache[address].data
            else:
                if use_coherence:
                    for cache in cache_list:
                        if cache.processor_id != self.processor_id and address in cache.cache:
                            if cache.cache[address].state == 'M':
                                print(f"[P{self.processor_id}] Writeback from [P{cache.processor_id}] for address {address}")
                                memory[address] = cache.cache
