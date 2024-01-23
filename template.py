import os ## Whenever you are using linux or windows then you need to import this os package becoz it will give you the generic path of the folder
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

projectName = "ML Project"

list_of_files=[
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/components/data_ingestion.py",
    f"src/{projectName}/components/data_transformation.py",
    f"src/{projectName}/components/model_trainer.py",
    f"src/{projectName}/pipelines/__init__.py",
    f"src/{projectName}/pipelines/training_pipeline.py",
    f"src/{projectName}/pipelines/prediction_pipeline.py",
    f"src/{projectName}/logger.py",
    f"src/{projectName}/utlis.py",
    "app.py",
    "Dockerfile",
    "Requirements.txt"
    "setup.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


else:
    logging.info(f"{filename} is already exists")