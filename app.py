from flask import Flask, render_template , request
import pickle
import pandas as pd
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
final_pt = pickle.load(open('final_pt.pkl' , 'rb'))
books = pickle.load(open('books.pkl' , 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl' , 'rb'))



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['No._of_Ratings'].values),
                           ratings=list(popular_df['Average_Ratings'].round(decimals = 1).values),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books' , methods = ['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(final_pt.index == user_input)[0][0]
    similar_books = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:7]

    data = []
    for i in similar_books:
        item = []

        temp_df = books[books['Book-Title'] == final_pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return render_template('recommend.html' , data = data)

if __name__ == '__main__':
    app.run(debug = True)