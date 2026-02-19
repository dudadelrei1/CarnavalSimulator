import random

class Estudante:
    def __init__(self, nome, estudo, cafe, fomo, posts_vistos, energia):
        self.__name = nome
        self.__study = estudo
        self.__cofee = cafe
        self.__fearof = fomo
        self.__post = posts_vistos
        self.__energy = energia

    def set_informations(self, nome, estudo,cafe, fomo, posts_vistos,energia):
        self.__name = nome
        self.__study = estudo
        self.__cofee = cafe
        self.__fearof = fomo
        self.__post = posts_vistos
        self.__energy = energia

    def get_informations(self):
        return {
            "Nome": self.__name,
            "Horas de Estudo": self.__study,
            "Nível de Café": self.__cofee,
            "FOMO": self.__fearof,
            "Posts Vistos": self.__post,
            "Energia": self.__energy
        } 
    
class FoliaFrustrada(Estudante):
    def nivel_sofrimento(self):
        dados = self.get_informations()
        sofrimento = (dados["FOMO"] * 2) + (dados["Posts Vistos"] / 10) + (dados["Nível de Café"] * 0.5) - dados["Energia"]
        resultado = sofrimento*100/350
        return max(0, resultado)

    def produtividade_real(self):
        dados = self.get_informations()
        sofrimento = self.nivel_sofrimento()
        produtividade = dados["Horas de Estudo"]*10 - (sofrimento * 0.3)

        if sofrimento > 15:
            produtividade *= 0.5  # colapso emocional

        return max(0, produtividade)
    
class CarnavalEmCasaAnalytics:
    def __init__(self, pessoas):
        self.pessoas = pessoas

    def rank_sofrimento(self):
        ranking = sorted(
            self.pessoas,
            key=lambda p: p.nivel_sofrimento(),
            reverse=True
        )
        return ranking
    
    def rank_produtividade(self):
        ranking = sorted(
            self.pessoas,
            key = lambda p: p.produtividade_real(),
            reverse=True
        )
        return ranking
    
    def media_fomo(self):
        if not self.pessoas:
            return 0
        media = sum(p.get_informations()["FOMO"] for p in self.pessoas) / len(self.pessoas)
        return media
    
    def coffee_drinker(self):
        if not self.pessoas:
            return None
        top = max(self.pessoas, key=lambda p: p.get_informations()["Nível de Café"])
        return top.get_informations()
    
    def discrepancia(self):
        if not self.pessoas: 
            return None
        top = max(self.pessoas, key=lambda p: p.nivel_sofrimento() - p.produtividade_real())
        return top.get_informations()

if __name__ == "__main__":
    nomes = ["Ana", "Duda", "Carlos", "João", "Marina", "Lucas", "Jessica", "Thiago", "Henrique", "Davi", "José", "Manoel"]
    escolhidos = random.sample(nomes, 5)
    pessoa = [FoliaFrustrada(escolhidos[i], random.randint(1,10), random.randint(0,100), random.randint(0,100), random.randint(0,1000), random.randint(0,100)) for i in range(5)]
    for p in pessoa:
        for chave, valor in p.get_informations().items():
            print(f'{chave}: {valor}')
        print(f'Sofrimento: {p.nivel_sofrimento():.4f}')
        print(f'Produtividade: {p.produtividade_real():.4f}')
        print()

    print("Ranking dos Mais Sofridos")
    people = CarnavalEmCasaAnalytics(pessoa)
    podio = people.rank_sofrimento()
    for idx, person in enumerate(podio, start=1):
        print(f'{idx} - {person.get_informations()["Nome"]} - {person.nivel_sofrimento():.2f}')
    print()

    print("Ranking dos Mais Produtivos")
    podio1 = people.rank_produtividade()
    for idx, person in enumerate(podio1, start=1):
        print(f'{idx} - {person.get_informations()["Nome"]} - {person.produtividade_real():.2f}')
    print()

    print(f"FOMO médio: {people.media_fomo():.2f}\n")
    print(f'Maior Consumidor de Café: {people.coffee_drinker()["Nome"]} - {people.coffee_drinker()["Nível de Café"]}')

    print(f'Aluno com Menor Rendimento (Mais sofrimento e menos produtividade): {people.discrepancia()["Nome"]}')
    print()
    