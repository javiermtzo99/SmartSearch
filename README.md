
# SmartSearch

SmartSearch is a platform that replicates the Canvas Discussions module with enhanced search capabilities using semantic search. It comprises three main components: analysis notebooks, a Flask backend, and a Next.js frontend.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Backend Installation](#backend-installation)
  - [Frontend Installation](#frontend-installation)
  - [Analysis Notebooks](#analysis-notebooks)
- [Usage](#usage)
  - [Running the Backend](#running-the-backend)
  - [Running the Frontend](#running-the-frontend)
  - [Running Analysis Notebooks](#running-analysis-notebooks)
- [Contributing](#contributing)
- [License](#license)

## Overview
SmartSearch enhances the Canvas Discussions module by using semantic search for better information retrieval. It allows users to interact with discussions more effectively, using semantic understanding to search through content.

## Project Structure
The repository is organized as follows:
```
SmartSearch/
│
├── backend/           # Flask backend for API and data processing
│   ├── app.py         # Main Flask application
│   ├── requirements.txt
│   └── ...            # Other backend files and directories
│
├── not_canvas/        # Next.js frontend for UI
│   ├── pages/
│   ├── components/
│   └── ...            # Other frontend files and directories
│
├── analysis/          # Jupyter notebooks for data exploration and testing
│   └── notebooks/
│
└── README.md          # Documentation
```

## Setup and Installation

### Prerequisites
Ensure you have the following installed on your system:
- **Python 3.7+**
- **Node.js 14.x+**
- **npm** (comes with Node.js)
- **Virtual Environment** (optional, but recommended)

### Backend Installation
The backend is a Flask application located in the **`backend/`** directory. To set up and run the backend:

1. **Navigate to the backend directory:**
   ```bash
   cd backend/
   ```

2. **Create a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the `backend/` directory with the following variables:
     ```
     CANVAS_API_URL=https://canvas.ubc.ca/
     CANVAS_API_KEY=your_api_key_here
     CANVAS_COURSE_ID=161721
     ```
   - Replace `your_api_key_here` with your actual Canvas API key.
   - Ensure `.env` is added to `.gitignore` to avoid pushing it to version control.

5. **Run the Flask application:**
   ```bash
   flask run --port=5001
   ```
   The backend will be accessible at [http://localhost:5001](http://localhost:5001).

6. **Testing the Backend:**
   - Visit [http://localhost:5001/discussions](http://localhost:5001/discussions) to see a list of discussions.
   - Use tools like Postman or `curl` to test the endpoints:
     ```bash
     curl http://localhost:5001/discussions
     ```

### Frontend Installation
The frontend is a Next.js application located in the **`not_canvas/`** directory.

1. **Navigate to the frontend directory:**
   ```bash
   cd not_canvas/
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the Next.js application in development mode:**
   ```bash
   npm run dev
   ```
   The frontend will be accessible at [http://localhost:3000](http://localhost:3000).

4. **Testing the Frontend:**
   - Visit [http://localhost:3000](http://localhost:3000) to interact with the SmartSearch UI.

### Analysis Notebooks
The **`analysis/`** directory contains Jupyter notebooks for testing and prototyping semantic search models.

1. **Navigate to the analysis directory:**
   ```bash
   cd analysis/
   ```

2. **Install Jupyter Notebook (if not already installed):**
   ```bash
   pip install jupyter
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
   Open and run the notebooks for analysis and testing.

## Usage

### Running the Backend
1. Ensure all dependencies are installed and environment variables are set up.
2. Start the Flask server:
   ```bash
   flask run --port=5001
   ```

### Running the Frontend
1. Ensure the backend is running.
2. Start the Next.js application:
   ```bash
   npm run dev
   ```

### Running Analysis Notebooks
1. Navigate to the **`analysis/`** directory.
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open and run the desired notebook.

## Contributing
Contributions are welcome! To contribute:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature-branch
   ```
3. **Make changes and commit:**
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push to your branch:**
   ```bash
   git push origin feature-branch
   ```
5. **Open a pull request.**

## License
This project is licensed under the [MIT License](LICENSE).
