import torch
import pathlib
import os


class ModelDetector:
    pathlib.WindowsPath = pathlib.PosixPath

    def __init__(self):
        print(os.getcwd())
        self.saw_crosswalk = False
        self.model = torch.hub.load('model/ultralytics', 'custom', path='model/best.pt', force_reload=True,
                                    trust_repo=True, source='local')

    def detect(self, frame, lookup_sign):
        results = self.model(frame)
        print(results)

        if lookup_sign == 'crosswalk' and self.saw_crosswalk:
            return {
                'lookup_sign': lookup_sign,
                'found': False
            }

        if lookup_sign in str(results):
            if lookup_sign == 'crosswalk':
                self.saw_crosswalk = True
            return {
                'lookup_sign': lookup_sign,
                'found': True
            }
        else:
            return {
                'lookup_sign': lookup_sign,
                'found': False
            }
