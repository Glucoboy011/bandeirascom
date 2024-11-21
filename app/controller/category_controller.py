from flask import Blueprint, render_template

from app.model.category import Category

category_bp = Blueprint('category', __name__)

categories = [Category(1, "Bandeiras de Estados"), Category(2, "Bandeiras de Países"), Category(3, "Bandeiras de Cidades e Clubes Esportivos "), Category(4, "Símbolos, Brasões e Outros")]

@category_bp.route('/categories')
def list_categories():
    return render_template('categories.html', categories=categories)
