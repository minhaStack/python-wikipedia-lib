import wikipedia
wikipedia.set_lang("pt")

print()
print('Resumo')
print(wikipedia.summary('Brasil'))

print()
print('Pesquisar')
print(wikipedia.search('Barão de Maua'))

print()
print('Visualizando uma página específica')
br = wikipedia.page("Brasilia")
print(br.title)
#print(br.content)
print(br.links[0])