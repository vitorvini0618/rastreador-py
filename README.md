#  Rastreador de Livros

Este é um projeto simples em Python que busca livros em um site de demonstração chamado [Books to Scrape](http://books.toscrape.com).  
O usuário digita o nome de um livro e o programa procura os títulos correspondentes nas primeiras 50 páginas do site.

##  O que o programa faz?

- Recebe o nome do livro que o usuário quer buscar
- Percorre as páginas do site
- Verifica se o nome aparece em algum título de livro
- Exibe até 6 resultados com nome e preço
- Informa se nenhum livro for encontrado

## Tecnologias usadas

- Python 3
- Biblioteca `requests` para acessar páginas web
- Biblioteca `BeautifulSoup` para fazer o scraping (extração de dados HTML)