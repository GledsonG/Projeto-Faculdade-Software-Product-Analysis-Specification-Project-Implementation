from supabase import create_client, Client


url = "https://dlmjmugouocyhspopdsb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsbWptdWdvdW9jeWhzcG9wZHNiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NzUwNjMsImV4cCI6MjA4NzU1MTA2M30.gblvuBxGpcX0OUwWm7I-9mFwywa31vL0jW_5B0sSlkc" 
supabase: Client = create_client(url, key)


def buscar_dados():
    try:
        resposta = supabase.table('produtos').select("*").execute()
        print("\n ESTOQUE ATUAL ")
        print(resposta.data)
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        

def cadastrar_produto():
    print("\n Cadastro novo de produto")
    nome = input ("Nome do produto:")
    preco = float(input("Preço:")) 
    marca = input ("Marca:")
    descricao = input ("Descrição:")       


    novo_item = {                #Não esquecer que esse é o dicionárioooooo e abaixo as chavesss...
        "nome": nome,
        "preco": preco,
        "marca": marca,
        "descricao": descricao
        }        

    try:
        supabase.table ("produtos").insert(novo_item).execute()
        print(f'/n {nome} cadastrado com sucesso')
    except Exception as e:
        print ('/n algo deu errado, por favor tente novamente!')


def deletar_produto():
    buscar_dados()
    id_para_deletar  = input("\n Digite o ID do produto que deseja excluir:")
    try:
       supabase.table ("produtos").delete().eq("id", id_para_deletar).execute() #aqui basicamente eu acesso a tabela "produtos", digo que quero deletar algo na coluna id e digo para deletar o que está dentro de id_para_deletar
       print ("Produto removido com sucesso!") 
    except Exception as e:
        print ("Não foi possivel deletar o produto, por favor tente novamente!")


def realizar_login():
    email_usuario = input("Digite o seu e-mail de acesso: ")
    senha_digitada = input("Digite a sua senha: ")
    
    try:
        resposta = supabase.table("usuarios").select("*").eq("email", email_usuario).execute()

        if len(resposta.data) > 0:
            usuario = resposta.data[0]
            
            if usuario['senha'] == senha_digitada:
                print(f"\n Sucesso! Bem-vindo, {usuario['nome']}!")
                return True
            else:
                print("\n Erro: Senha incorreta.")
                return False
        else:
            print("\n Erro: E-mail não cadastrado.")
            return False
    except Exception as e:
        print(f"\n Erro de conexão: {e}")
        return False
    

if __name__ == "__main__":
    if realizar_login():
        while True: 
            print("\n 1 - Ver Estoque")
            print("2 - Cadastrar Produto")
            print("3 - Deletar produto")
            print("4 - Sair")
            opcao = input("\nO que deseja fazer? ")

            if opcao == "1":    
                buscar_dados()
            elif opcao == "2":
                cadastrar_produto()
            elif opcao =="3":
                deletar_produto()
            elif opcao == "4":
                print("Saindo... Até logo!")
                break
            else:
                print("Opção inválida!")