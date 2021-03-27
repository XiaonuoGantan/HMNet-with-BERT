from typing import Dict


class TrainTask(object):
    """Encapsulate `BatchGeneration` and `Rougue/MeteorEval`"""

    def __init__(self, batch_gen, evaluator):
        self.batch_gen = batch_gen
        self.evaluator = evaluator

    @classmethod
    def setup(cls, conf: Dict, save_dir: str):
        """Setup a TrainTask instance"""
        raise NotImplementedError