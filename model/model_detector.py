import torch
import pathlib
import os
import time


class ModelDetector:
    pathlib.WindowsPath = pathlib.PosixPath

    def __init__(self):
        print(os.getcwd())
        self.saw_crosswalk = False
        self.last_sent_sign_time = time.time()
        self.model = torch.hub.load('model/ultralytics', 'custom', path='model/best.pt', force_reload=True,
                                    trust_repo=True, source='local')

    def detect(self, frame, lookup_sign):
        current_time = time.time()
        results = self.model(frame)
        print(results)



        if current_time - self.last_sent_sign_time < 4:
            self.last_sent_sign_time = current_time
            return {
                'lookup_sign': lookup_sign,
                'found': "none"
            }

        if lookup_sign == 'stop':
            if lookup_sign in str(results):
                self.last_sent_sign_time = current_time
                return {
                    'lookup_sign': lookup_sign,
                    'found': 'stop'
                }
            else:
                self.last_sent_sign_time = current_time
                return {
                    'lookup_sign': lookup_sign,
                    'found': 'none'
                }

        if lookup_sign == 'crosswalk':

            if lookup_sign in str(results):
                if self.saw_crosswalk:
                    self.last_sent_sign_time = current_time
                    return {
                        'lookup_sign': lookup_sign,
                        'found': 'none'
                    }
                self.saw_crosswalk = True
                self.last_sent_sign_time = current_time
                return {
                    'lookup_sign': lookup_sign,
                    'found': 'crosswalk'
                }
            else:
                self.saw_crosswalk = False
                self.last_sent_sign_time = current_time
                return {
                    'lookup_sign': lookup_sign,
                    'found': 'parking'
                }


