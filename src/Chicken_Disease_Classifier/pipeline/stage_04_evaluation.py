from Chicken_Disease_Classifier.config.configuration import ConfigurationManager
from Chicken_Disease_Classifier.components.evaluation import Evaluation
from Chicken_Disease_Classifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()