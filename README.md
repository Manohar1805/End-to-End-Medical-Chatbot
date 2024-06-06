# End-to-end Medical Chatbot using Llama2

## Introduction
This project aims to create an end-to-end medical chatbot using Meta's Llama2 model, LangChain, Flask, and Pinecone for vector storage. The chatbot is designed to provide users with medical information based on the input it receives.

## Project Repository
You can find the project repository at the following link: [Project Repo](https://github.com/)

## Getting Started

### Step 1: Clone the Repository
First, clone the repository to your local machine.

```sh
git clone https://github.com/your-repository-url
cd your-repository-folder
```

### Step 2: Create a Conda Environment
Create and activate a new conda environment with Python 3.8.

```sh
conda create -n mchatbot python=3.8 -y
conda activate mchatbot
```

### Step 3: Install Requirements
Install the required Python packages from the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your Pinecone credentials.

```sh
echo "PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" >> .env
echo "PINECONE_API_ENV=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" >> .env
```

### Step 5: Download the Quantized Model
Download the Llama 2 quantized model and place it in the `model` directory.

#### Download the Llama 2 Model:
- Model file: `llama-2-7b-chat.ggmlv3.q4_0.bin`
- Download link: [Llama 2 Model on Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

### Step 6: Store the Index
Run the following command to store the index using Pinecone.

```sh
python store_index.py
```

### Step 7: Start the Application
Finally, run the following command to start the Flask application.

```sh
python app.py
```

### Access the Application
Open your web browser and navigate to `localhost` to access the medical chatbot.

## Tech Stack Used
- **Python**
- **LangChain**
- **Flask**
- **Meta Llama2**
- **Pinecone**

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This version provides clear, step-by-step instructions on setting up and running the medical chatbot project, making it easier for others to follow along and get started.
