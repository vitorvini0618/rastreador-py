import requests
from bs4 import BeautifulSoup

produto = input(" Digite o nome do livro para buscar: ").lower()

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

encontrados = 0  

try:
    for pagina in range(1, 51):
        url = base_url.format(pagina)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        livros = soup.select("article.product_pod")

        for livro in livros:
            titulo = livro.h3.a["title"]
            preco = livro.select_one("p.price_color").text

            if produto in titulo.lower():
                print(f" {titulo} —  {preco}")
                encontrados += 1

            if encontrados == 6: 
                break

        if encontrados == 6:
            break

    if encontrados == 0:
        print("Nenhum livro encontrado com esse nome.")

except requests.RequestException as e:
    print(" Ocorreu um erro ao acessar o site", e)
