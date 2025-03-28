from src.TextSummarization.logging import logger
from src.TextSummarization.pipeline.stage_1_ingestion import DataIngestionTrainingPipeline 
from src.TextSummarization.pipeline.stage_2_data_transformation import DataTransformationTrainingPipeline
from src.TextSummarization.pipeline.stage_3_model_trainer import ModelTrainerPipeline
from src.TextSummarization.pipeline.stage_4_model_eval import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipepine = DataIngestionTrainingPipeline()
    data_ingestion_pipepine.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.init_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try: 
    logger.info(f"stage {STAGE_NAME} initiated")
    model_eval_pipeline = ModelEvaluationPipeline()
    model_eval_pipeline.initate_model_eval()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e : 
    logger.exception(e)
    raise e