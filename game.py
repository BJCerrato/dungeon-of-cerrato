player = {
    "hp": 30,
    "ataque": 5,
    "ouro":0,
    "inventario":[],
    "pontuacao":0    
}
inimigo = {
    "nome": "Rato de Dungeon",
    "hp":15,
    "ataque":3
}

def exibir_status():
    print("=" * 30)
    print(f"  HP: {player['hp']}")
    print(f"  Ouro: {player['ouro']}")
    print(f"  Pontuação: {player['pontuacao']}")
    print("=" * 30)
    
def combate():
    print(f"\nUm {inimigo['nome']} apareceu!")
    print(f"HP do inimigo: {inimigo['hp']}\n")
    
    while inimigo["hp"] > 0 and player["hp"] > 0:
        print("O que você faz?")
        print("1 - Atacar")
        print("2 - Fugir")
        acao = input("> ")
        
        if acao == "1":
            print(f"Player ataca! Inimigo perde {player['ataque']} HP")
            inimigo["hp"] = inimigo["hp"] - player["ataque"]
            if inimigo["hp"] > 0:
                print(f"Inimigo ataca! Player perde {inimigo['ataque']} HP")
                if (player["hp"] - inimigo["ataque"]) > 0:
                    player["hp"]= player["hp"] - inimigo["ataque"]
                    exibir_status()
                else:
                    player["hp"] = 0
                    exibir_status()
                    print("Player perdeu!")
                    print("GAME OVER")
            else:
                player["ouro"] = player["ouro"] + 2
                player["pontuacao"] = player["pontuacao"] + 50
                print("Player venceu!")
                exibir_status()
        elif acao == "2":
            print("Player fugiu!")
            break
        else:
            print("Ação inválida! Selecione uma das opções disponíveis!")
    
if __name__=="__main__":
    exibir_status()
    combate()