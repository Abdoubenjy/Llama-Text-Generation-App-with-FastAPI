
# 🤖 FastAPI Language Model Application

A web-based application powered by **FastAPI** and **Hugging Face Transformers**, leveraging the `meta-llama/Llama-3.2-1B` language model for text generation. 🚀

## 🌟 Features

- **Interactive Frontend**: Enter text via a clean interface to generate responses.
- **Backend API**: Use the `/check` endpoint to verify the model and tokenizer status.
- **Auto GPU Utilization**: Automatically detects and utilizes GPU if available for faster processing.
- **Custom Configuration**: Securely loads API keys and model configuration from a `config.json` file.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abdoubenjy/Llama-Text-Generation-App-with-FastAPI.git
   cd Llama-Text-Generation-App-with-FastAPI
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration**:
   Create a `config.json` file with the following structure:
   ```json
   {
     "HF_TOKEN": "your_hugging_face_api_token"
   }
   ```

---

## 🚀 Usage

1. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Interface**:
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). You’ll find an interactive interface to input text and view generated responses.

3. **API Endpoints**:
   - **Frontend**: `/` (HTML interface for text input and responses)
   - **Model Check**: `/check` (JSON response with model and tokenizer status)

---

## 📂 Project Structure

```plaintext
.
├── main.py              # FastAPI application script
├── config.json          # Configuration file for API tokens
├── templates/           # HTML templates for the frontend
│   └── index.html       # Main page template
├── static/              # Static files (CSS, JS, images)
└── requirements.txt     # Python dependencies
```

---

## ⚙️ Configuration

- **Model ID**: The script uses the `meta-llama/Llama-3.2-1B` model by default.
- **API Key**: Your Hugging Face API token is securely loaded from `config.json`.
- **Environment**: The application automatically uses the GPU if available (`device_map="auto"`).

