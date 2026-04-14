# Smart Resume Matcher 🚀

An automated tool built with **Python** that evaluates how well a resume matches a specific job description. This project uses Natural Language Processing (NLP) to help candidates optimize their resumes for Applicant Tracking Systems (ATS).

## 📌 Project Overview
As a final-year student at **Pondicherry Technological University**, I developed this tool to bridge the gap between job requirements and technical resumes. It extracts text from a PDF, processes the language, and calculates a similarity score using mathematical algorithms.

## 🛠️ Features
* **PDF Extraction**: Uses `PyPDF2` to read and parse resume content like skills and projects.
* **Text Vectorization**: Converts text data into numerical vectors using `CountVectorizer`.
* **Smart Matching**: Implements **Cosine Similarity** to provide a match percentage.
* **Real-time Feedback**: Categorizes results into "Great Match," "Good Match," or "Low Match" based on the score.

## 💻 Technical Skills Used
* **Languages**: Python
* **Libraries**: PyPDF2, Scikit-learn
* **Database Management**: SQL (MySQL)
* **Core Concepts**: NLP, Data Structures & Algorithms, Object-Oriented Programming (OOP)

## 📂 How to Run
1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed: `pip install PyPDF2 scikit-learn`.
3. Place your resume in the folder and rename it to `SOUNDARYA_ RESUME_2026.pdf` (or update the filename in the code).
4. Paste the job description requirements into `job.txt`.
5. Run the script:
   ```bash
   python matcher.py

👤 Author - Soundarya Devi  
