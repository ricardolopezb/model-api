import torch
import pathlib
import os


class ModelDetector:
    pathlib.WindowsPath = pathlib.PosixPath

    def __init__(self):
        print(os.getcwd())
        self.model = torch.hub.load('model/ultralytics', 'custom', path='model/best.pt', force_reload=True,
                                    trust_repo=True, source='local')

    def detect(self, frame, lookup_sign):
        results = self.model(frame)
        print(results)
        if lookup_sign in str(results):
            return {
                'lookup_sign': lookup_sign,
                'found': True
            }
        else:
            return {
                'lookup_sign': lookup_sign,
                'found': False
            }
