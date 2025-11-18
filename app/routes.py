from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.models import User, Post, Comment

@app.route("/")
@login_required
def index():
    # Pobieranie wszystkich postów, od najnowszych
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Sprawdzenie czy użytkownik istnieje
        if User.query.filter_by(username=username).first():
            flash('Taka nazwa użytkownika jest już zajęta.', 'danger')
            return redirect(url_for('register'))
        
        # Tworzenie użytkownika
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Konto utworzone! Możesz się zalogować.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        # Prosta weryfikacja hasła (w produkcji użyj hashowania!)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Błędny login lub hasło.', 'danger')
            
    return render_template('login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/post/new", methods=['POST'])
@login_required
def new_post():
    content = request.form.get('content')
    if content:
        post = Post(content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Twój post został dodany!', 'success')
    return redirect(url_for('index'))

@app.route("/comment/<int:post_id>", methods=['POST'])
@login_required
def new_comment(post_id):
    content = request.form.get('content')
    post = Post.query.get_or_404(post_id)
    if content:
        comment = Comment(content=content, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Komentarz dodany!', 'success')
    return redirect(url_for('index'))
