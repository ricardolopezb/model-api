import torch
import pathlib
import os


class ModelDetector:
    pathlib.WindowsPath = pathlib.PosixPath

    def __init__(self):
        print(os.getcwd())
        self.model = torch.hub.load('model/ultralytics', 'custom', path='model/best.pt', force_reload=True,
                                    trust_repo=True, source='local')

    def detect(self, frame, lookupSignal):
        print("***************** ENTERED MODEL DETECTION")
        results = self.model(frame)
        print(results)
        if lookupSignal in str(results):
            return f"Se encontró la señal '{lookupSignal}'."
        else:
            return f"No se encontró la señal '{lookupSignal}'."
