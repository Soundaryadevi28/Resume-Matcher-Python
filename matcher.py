import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Function to read the PDF
def read_resume(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# 2. Start the process
print("Reading your resume and job description...")

# Get the text from your files
resume_text = read_resume('SOUNDARYA_ RESUME_2026.pdf')

with open('job.txt', 'r') as f:
    job_text = f.read()

# 3. The Math Part (The Matching)
content = [resume_text, job_text]
cv = CountVectorizer()
matrix = cv.fit_transform(content)
similarity_matrix = cosine_similarity(matrix)

# Calculate percentage
match_percentage = similarity_matrix[0][1] * 100
match_percentage = round(match_percentage, 2)

# 4. Show the Results
print("-" * 30)
print(f"MATCH SCORE: {match_percentage}%")
print("-" * 30)

if match_percentage > 70:
    print("Result: Great match! You should apply.")
elif match_percentage > 40:
    print("Result: Good match, but maybe add more keywords from the job post.")
else:
    print("Result: Low match. Check if you missed some technical skills.")