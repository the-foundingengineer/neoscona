from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

# Postgres Connection Details
DB_USER = 'postgres'
DB_PASS = 'IGOSDP2022'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'neoscona_db'

def get_db_connection():
    conn = psycopg2.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME
    )
    return conn

@app.route('/')
def index():
    return render_template('neoscona.html')

@app.route('/blog')
def blog():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    # Fetch all posts from postgres
    cur.execute('SELECT * FROM posts ORDER BY created_at DESC')
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('blog.html', posts=posts)

@app.route('/admin', methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        content = request.form['content']
        image_url = request.form['image_url']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO posts (title, category, content, image_url) VALUES (%s, %s, %s, %s)',
            (title, category, content, image_url)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('blog'))
    
    return render_template('admin.html')

if __name__ == '__main__':
    # Ensure images directory is handled correctly if needed, 
    # but usually Flask serves from /static. 
    # Since our HTML uses 'images/', we can use a custom static route if needed.
    app.run(debug=True, port=5000)
