import customtkinter as ctk
from supabase import create_client


ctk.set_appearance_mode("light") 
COR_FUNDO = "#FFFFFF"     
COR_DOURADO = "#FFC400"   
COR_TEXTO = "#4A4A4A"     


url = "https://dlmjmugouocyhspopdsb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsbWptdWdvdW9jeWhzcG9wZHNiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NzUwNjMsImV4cCI6MjA4NzU1MTA2M30.gblvuBxGpcX0OUwWm7I-9mFwywa31vL0jW_5B0sSlkc"
supabase = create_client(url, key)

def exibir_estoque():
    limpar_tela()
    
    ctk.CTkLabel(janela, text="ESTOQUE ATUAL", font=("Bodoni", 22, "bold"), text_color=COR_DOURADO).pack(pady=20)

    
    frame_lista = ctk.CTkScrollableFrame(janela, width=400, height=400, fg_color="transparent")
    frame_lista.pack(pady=10, padx=20)

    try:
        resposta = supabase.table("produtos").select("*").execute()
        for item in resposta.data:
          
            card = ctk.CTkFrame(frame_lista, fg_color="#F9F9F9", corner_radius=8, border_width=1, border_color="#E0E0E0")
            card.pack(fill="x", pady=5, padx=5)

          
            info = f"{item['nome']} - {item['marca']}\nR$ {item['preco']:.2f}"
            ctk.CTkLabel(card, text=info, font=("Arial", 12), justify="left", text_color=COR_TEXTO).pack(side="left", padx=15, pady=10)

           
            btn_del = ctk.CTkButton(card, text="🗑", width=30, fg_color="#FF4C4C", hover_color="#C0392B",
                                    command=lambda id_prod=item['id']: deletar_e_atualizar(id_prod))
            btn_del.pack(side="right", padx=10)

    except Exception as e:
        ctk.CTkLabel(frame_lista, text="Erro ao carregar dados").pack()

    ctk.CTkButton(janela, text="VOLTAR", fg_color="transparent", text_color=COR_DOURADO, border_width=1, border_color=COR_DOURADO,
                  width=320, command=exibir_menu_principal).pack(pady=20)
                  
def deletar_e_atualizar(id_prod):
    try:
        supabase.table("produtos").delete().eq("id", id_prod).execute()
        exibir_estoque() 
    except Exception as e:
        print(f"Erro ao deletar: {e}")


def limpar_tela():
    """Remove todos os elementos da janela atual para desenhar a próxima"""
    for widget in janela.winfo_children():
        widget.destroy()


def salvar_produto(nome_ent, marca_ent, preco_ent, desc_ent):
    nome = nome_ent.get()
    marca = marca_ent.get()
    preco = preco_ent.get()
    descricao = desc_ent.get()
    

    if nome and preco:
        try:
            supabase.table("produtos").insert({
                "nome": nome, 
                "marca": marca,
                "preco": float(preco),
                "descricao": descricao
            }).execute()
            exibir_menu_principal() 
        except Exception as e:
            print(f"Erro ao salvar: {e}")


def exibir_tela_cadastro():
    limpar_tela() 
    

    ctk.CTkLabel(janela, text="NOVO PRODUTO", font=("Bodoni", 22, "bold"), text_color=COR_DOURADO).pack(pady=30)

    
    ent_nome = ctk.CTkEntry(janela, placeholder_text="Nome do Item", width=320, height=40, border_color=COR_DOURADO, fg_color="#FAFAFA")
    ent_nome.pack(pady=8)

    ent_marca = ctk.CTkEntry(janela, placeholder_text="Marca", width=320, height=40, border_color=COR_DOURADO, fg_color="#FAFAFA")
    ent_marca.pack(pady=8)

    ent_preco = ctk.CTkEntry(janela, placeholder_text="Preço de Venda", width=320, height=40, border_color=COR_DOURADO, fg_color="#FAFAFA")
    ent_preco.pack(pady=8)

    ent_desc = ctk.CTkEntry(janela, placeholder_text="Descrição / Detalhes", width=320, height=40, border_color=COR_DOURADO, fg_color="#FAFAFA")
    ent_desc.pack(pady=8)

    
    ctk.CTkButton(janela, text="SALVAR NO ESTOQUE", fg_color=COR_DOURADO, hover_color="#B8860B", text_color="white", 
                  width=320, height=45, font=("Arial", 13, "bold"), 
                  command=lambda: salvar_produto(ent_nome, ent_marca, ent_preco, ent_desc)).pack(pady=25)
    
    ctk.CTkButton(janela, text="VOLTAR", fg_color="transparent", text_color=COR_DOURADO, border_width=1, border_color=COR_DOURADO,
                  width=320, command=exibir_menu_principal).pack()
    

def exibir_menu_principal():
    limpar_tela() 
    
    ctk.CTkLabel(janela, text="Le'Prado", font=("Bodoni", 35, "bold"), text_color=COR_DOURADO).pack(pady=(50, 5))
    ctk.CTkLabel(janela, text="GESTÃO DE ESTOQUE", font=("Arial", 11), text_color="#A0A0A0").pack(pady=(0, 50))

    estilo_btn = {"width": 280, "height": 45, "fg_color": COR_DOURADO, "hover_color": "#B8860B", "text_color": "white", "font": ("Arial", 12, "bold")}

    ctk.CTkButton(janela, text="VER ESTOQUE", command=exibir_estoque, **estilo_btn).pack(pady=10)
    
    ctk.CTkButton(janela, text="CADASTRAR PRODUTO", command=exibir_tela_cadastro, **estilo_btn).pack(pady=10)
    
    ctk.CTkButton(janela, text="SAIR DO SISTEMA", fg_color="#F2F2F2", text_color="#7F7F7F", width=280, command=janela.quit).pack(pady=40)


def realizar_login_gui():
    email = entry_email.get()
    senha = entry_senha.get()
    try:
        res = supabase.table("usuarios").select("*").eq("email", email).execute()
        if len(res.data) > 0 and res.data[0]['senha'] == senha:
            exibir_menu_principal()
        else:
            label_aviso.configure(text="Credenciais Inválidas", text_color="red")
    except Exception:
        label_aviso.configure(text="Erro de Conexão", text_color="orange")


janela = ctk.CTk()
janela.geometry("450x650") 
janela.title("Le'Prado")
janela.configure(fg_color=COR_FUNDO)

ctk.CTkLabel(janela, text="Le'Prado", font=("Georgia", 30, "bold"), text_color=COR_DOURADO).pack(pady=(80, 40))

entry_email = ctk.CTkEntry(janela, placeholder_text="Usuário", width=320, height=45, border_color=COR_DOURADO, fg_color="#FDFDFD")
entry_email.pack(pady=10)

entry_senha = ctk.CTkEntry(janela, placeholder_text="Senha", width=320, height=45, border_color=COR_DOURADO, fg_color="#FDFDFD", show="*")
entry_senha.pack(pady=10)

label_aviso = ctk.CTkLabel(janela, text="")
label_aviso.pack(pady=10)

ctk.CTkButton(janela, text="ACESSAR PAINEL", fg_color=COR_DOURADO, hover_color="#ECAF12", text_color="white", 
              width=320, height=45, font=("Arial", 13, "bold"), command=realizar_login_gui).pack(pady=20)

janela.mainloop()