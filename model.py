from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def resume_score(resume_text, job_description):

    documents = [resume_text, job_description]

    cv = CountVectorizer()
    matrix = cv.fit_transform(documents)

    similarity = cosine_similarity(matrix)

    score = similarity[0][1] * 100

    return round(score,2)