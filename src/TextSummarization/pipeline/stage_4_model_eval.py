from src.TextSummarization.config.configuration import  ConfigurationManager 
from src.TextSummarization.components.model_eval import ModelEvaluation
from src.TextSummarization.logging import logger 

class ModelEvaluationPipeline:
    def __init__(self):
        pass 
    def initate_model_eval(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_eval_config()
        model_eval = ModelEvaluation(config= model_eval_config)
        model_eval.convert()