🥗 Diet Recommendation System
The Diet Recommendation System is a Python-based application designed to suggest personalized diet plans based on a user’s health metrics and goals. It utilizes machine learning models to analyze user input such as age, BMI, activity level, and dietary preferences to recommend healthy and tailored meal options.
________________________________________
✨ Features
-	🧠 Machine Learning-based diet predictions
-	📍 User input for personalized recommendations
-	📊 Nutritional analysis & health metrics
-	🐳 Dockerized for easy deployment
-	💻 Interactive interface using Streamlit
-	🗣️ Chatbot for dietary queries powered by OpenAI
________________________________________
📁 Project Structure
```
diet-recommendation-system/
├── Assets/                  # Images, icons, logos
├── Data/                   # Dataset folder (add dataset.csv or dataset.csv.gz)
├── Docs/                   # Documentation and references
├── FastAPI_Backend/
│   ├── main.py             # FastAPI application entry point
│   ├── model.py            # ML model logic and processing
│   ├── Dockerfile          # Backend Docker container setup
│   ├── requirements.txt    # Backend dependencies
│   └── .dockerignore
├── Streamlit_Frontend/
│   ├── pages/
│   │   ├── 1.Diet_Recommendation.py
│   │   └── 2.Custom_Food_Search.py
│   ├── ImageFinder/
│   │   ├── __init__.py
│   │   └── ImageFinder.py  # Custom food image tools
│   ├── Generate_Recommendation.py
│   ├── Hello.py            # Chatbot UI
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
├── food-recommendation.env  # Environment variables
├── docker-compose.yml       # Combined setup for backend + frontend
├── LICENSE
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── .gitignore
└── .gitattributes
```
________________________________________
## 🔧 Technologies Used

•	Python 3.10+
•	pandas, scikit-learn, NumPy
•	Streamlit (for UI)
•	FastAPI (for backend API)
•	Docker & Docker Compose
•	OpenAI GPT for chatbot
________________________________________
## 📈 Dataset
The model uses a dataset containing:
•	Nutritional features:
o	Calories, FatContent, SaturatedFatContent, CholesterolContent,
o	SodiumContent, CarbohydrateContent, FiberContent, SugarContent, ProteinContent
•	Metadata:
o	Name, CookTime, PrepTime, TotalTime
•	Additional Fields:
o	RecipeIngredientParts (list of ingredients)
o	RecipeInstructions (list of steps)
Location:
Place dataset.csv or dataset.csv.gz inside:
/Data/
If using dataset.csv.gz, the backend automatically decompresses it.
________________________________________
## 🔊 Chatbot Integration
We use OpenAI GPT-3.5-turbo to provide helpful dietary responses to user queries.
🔗 Endpoint
POST /chat/
## 🛡️ Security Note
Add a .env file at project root or in the backend folder:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Ensure .env is added to .gitignore to protect your key.
## 📅 Example
## User Input:
What are some high-protein vegetarian breakfast options?
## Bot Output:
Some high-protein vegetarian options include Greek yogurt with chia seeds, boiled eggs with whole grain toast, or a protein smoothie with almond butter and banana.
________________________________________
## 🚚 Installation
⚙️ Option 1: Run Locally
# Clone the repository
git clone https://github.com/codewithadityaj/diet-recommendation-system.git
cd diet-recommendation-system

# Start with Docker Compose
docker-compose up --build
________________________________________
## 📁 Required Files & Dependencies
## Backend
```
# FastAPI_Backend/requirements.txt
fastapi==0.88.0
uvicorn==0.20.0
numpy==1.24.1
scikit-learn==1.1.3
pandas==1.5.1
pydantic==1.10.4
openai>=1.0.0
python-dotenv
```
## Frontend
```
# Streamlit_Frontend/requirements.txt
streamlit
requests
```
________________________________________
## ✨ Coming Soon
-	User login & health tracking
-	Food image recognition
-	MongoDB integration
________________________________________
✉️ Contact
Maintained by Aditya Ashok Jadhav
________________________________________
⚠️ If you encounter issues, make sure both the backend (FastAPI) and frontend (Streamlit) containers are running and accessible.
