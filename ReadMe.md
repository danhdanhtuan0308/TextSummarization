# Text Summarization using Hugging Face

This project implements a text summarization pipeline using Hugging Face's Transformers library. The pipeline includes data ingestion, data transformation, model training, evaluation, and prediction, with APIs for training and batch predictions.

---

## **Overview**

The goal of this project is to build an end-to-end text summarization system. It leverages a pre-trained model (e.g., Pegasus) from Hugging Face, fine-tuned on the SAMSum dataset, to generate concise summaries of dialogues or text inputs. The project is modular, containerized with Docker, and includes a FastAPI interface for ease of use.

---

## **Workflows**

1. **Config.yaml**  
   - Stores configuration details like file paths, dataset URLs, and model checkpoints.

2. **Params.yaml**  
   - Contains training hyperparameters such as batch size, learning rate, and number of epochs.

3. **Config Entity**  
   - Defines data classes to manage configurations for each pipeline stage.

4. **Configuration Manager**  
   - Reads YAML files and initializes directories for storing artifacts.

5. **Pipeline Components**  
   - **Data Ingestion**: Downloads and extracts the dataset (e.g., SAMSum).  
   - **Data Transformation**: Preprocesses and tokenizes the data for model input.  
   - **Model Trainer**: Fine-tunes the summarization model.  
   - **Model Evaluation**: Assesses model performance using ROUGE metrics.

6. **Pipeline Creation**  
   - **Training Pipeline**: Combines all components to train the model.  
   - **Inference Pipeline**: Generates summaries for new text inputs.

7. **Frontend and API**  
   - **Training API**: Triggers the training pipeline via an endpoint.  
   - **Batch Prediction API**: Provides summaries for multiple inputs.

---

## **Project Structure**

```
TextSummarization/
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── app.py                 # FastAPI application
├── Dockerfile             # Docker configuration
├── image.png              # Project image (optional)
├── main.py                # Main script to run the pipeline
├── params.yaml            # Training hyperparameters
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── template.py            # Template for project setup
├── .github/
│   └── workflows/         # CI/CD workflows (optional)
├── artifacts/             # Output directory
│   ├── data_ingestion/    # Downloaded dataset
│   ├── data_transformation/ # Preprocessed data
│   ├── model_evaluation/  # Evaluation results
│   └── model_trainer/     # Trained models
├── config/
│   └── config.yaml        # Configuration file
├── logs/
│   └── continuous_logs.log # Log file
├── research/              # Jupyter notebooks for experimentation
│   ├── 1_data_ingestion.ipynb
│   ├── 2_data_transformation.ipynb
│   ├── 3_model_trainer.ipynb
│   ├── 4_model_evaluation.ipynb
│   └── textsummarizer.ipynb
├── src/
│   └── TextSummarization/ # Source code
└── summarizer-data/       # Raw dataset files
    ├── samsum-test.csv
    ├── samsum-train.csv
    └── samsum-validation.csv
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/TextSummarization.git
cd TextSummarization
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
python app.py
```
- Access the FastAPI server at `http://127.0.0.1:8000`.

---

## **Docker Instructions**

### **1. Build the Docker Image**
```bash
docker build -t text-summarization .
```

### **2. Run the Docker Container**
```bash
docker run -p 8000:8000 text-summarization
```
- The API will be available at `http://localhost:8000`.

---

## **Key Features**

- **Data Ingestion**: Downloads and preprocesses the SAMSum dataset.
- **Data Transformation**: Tokenizes and prepares data for model training.
- **Model Training**: Fine-tunes a Hugging Face model (e.g., Pegasus) for summarization.
- **Model Evaluation**: Measures performance using ROUGE metrics.
- **Prediction API**: Provides text summarization via a FastAPI endpoint.

---

## **Technologies Used**

- **Python**: Core programming language.
- **FastAPI**: Web framework for API development.
- **Hugging Face Transformers**: Library for pre-trained models and tokenizers.
- **Docker**: Containerization for deployment.
- **Jupyter Notebooks**: Research and experimentation.

---

## **Usage**

### **Training the Model**
- Use the `/train` endpoint to start the training pipeline:
```bash
curl -X POST "http://127.0.0.1:8000/train"
```

### **Making Predictions**
- Use the `/predict` endpoint for batch predictions:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"texts": ["Your text here"]}'
```

---

## **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.


## Testing prediction 
Example : The old lighthouse stood silent, its beam long extinguished. Every night, Ella climbed its spiral stairs, clutching a lantern. She’d heard the tales—ships lost to the fog, guided once by that light. Her grandfather had been the last keeper, his logbook filled with cryptic notes: “They call from the deep.” Tonight, the fog was thick, the air heavy with whispers. She lit the lantern, and the mist parted, revealing countless glowing eyes below the waves. A voice echoed, “Thank you.” Ella smiled, knowing she’d rekindled more than light—she’d honored a pact older than memory. 

Output : ![alt text](image-1.png)