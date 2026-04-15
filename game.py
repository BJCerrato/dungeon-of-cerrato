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
    
if __name__=="__main__":
    exibir_status()