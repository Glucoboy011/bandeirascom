from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product
import random

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Bandeiras de Estados"), Category(2, "Bandeiras de Países"), Category(3, "Bandeiras de Cidades e Clubes Esportivos "), Category(4, "Símbolos e Brasões")]
products = [
    Product(7, "Bandeira do Acre", 35.99, 1, "1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
    ]),
    Product(1, "Bandeira do Afeganistão", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
    ]),
    Product(2, "Bandeira da Alemanha", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-alemanha-reta.jpg",
    ]),
    Product(11, "Bandeira do Rio Grande do Sul", 35.99, 1, "Tamanho 1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
    ]),
    Product(13, "Bandeira do Estado de São Paulo", 35.99, 1, "Tamanho 1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
    ]),
    Product(4, "Bandeira Oficial do Brasil - Modelo Bordado em Cetim", 69.99, 2, "Tamanho 2.25x3.20m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
    ]),
    Product(14, "Bandeiras de Municípios Brasileiros", 99.99, 3, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
    ]),
    Product(8, "Bandeira de Goiás", 35.99, 1, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-goias-reta.jpg",
    ]),
    Product(10, "Bandeira do Estado do Rio de Janeiro", 35.99, 1, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-de-janeiro-reta.jpg",
    ]),
    Product(12, "Bandeira de Santa Catarina", 35.99, 1, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-santa-catarina-reta.jpg",
    ]),
    Product(9, "Bandeira do Paraná", 35.99, 1, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-parana-reta.jpg",
    ]),
    Product(6, "Bandeira do Reino Unido", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-reino-unido-reta.jpg",
    ]),
    Product(5, "Bandeira dos Estados Unidos", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-estados-unidos-reta.jpg",
    ]),
    Product(3, "Bandeira da Argentina", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-argentina-reta.jpg",
    ]),
    Product(14, "Bandeira de Clubes Esportivos", 89.99, 3, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/clubes/bandeira-personalizada-clube-02.jpg",
    ]),
    Product(15, "Bandeira LGBT+", 39.99, 4, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-gay-reta.jpg", 
    ]),
        Product(16, "Flâmula Império do Brasil", 45.99, 4, "Tamanho 1.56x1.90m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38",
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38",
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38",
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38",
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38",
        "https://www.bandeira1.com.br/lojas/00002028/prod/flamulas/flamula-imperial-do-brasil-1823-1889.jpg?cccfc=2d4c0f38", 
    ]),




]

@home_bp.route('/')
def home():
    # Seleciona 3 produtos aleatórios
    featured_products = random.sample(products, 4)
    return render_template('index.html', categories=categories, products=featured_products)
