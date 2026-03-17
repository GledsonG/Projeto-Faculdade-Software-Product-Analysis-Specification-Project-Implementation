# 🧴 Sistema Le' Prado - Gestão de Inventário

Este repositório contém o código-fonte do sistema de gestão de produtos da **NikBelo*. O projeto adota uma arquitetura em **três camadas** (Front-end, Back-end e Database).

---

## 🏛️ Arquitetura do Projeto

### 🎨 Camada de Apresentação (Front-end)
* Desenvolvida em **Python** utilizando a biblioteca **CustomTkinter**.
* Interface inspirada na estética minimalista "Branco e Dourado".
* Sistema de navegação em **tela única** para otimização de fluxo e memória.

### 🧠 Camada de Lógica de Negócios (Back-end)
* Implementação de rotinas de autenticação de usuários.
* Processamento e validação de dados de entrada para o inventário (Nome, Marca, Preço e Descrição).
* Gerenciamento de estados da aplicação e controle de fluxo.

### 💾 Camada de Persistência (Database)
* Integração em tempo real com o **Supabase** (PostgreSQL na nuvem).
* Implementação de **Row Level Security (RLS)**, garantindo que as transações de dados ocorram em um ambiente seguro e controlado.

---


🚀 Funcionalidades Principais

Autenticação de Acesso: Sistema de login seguro com validação de credenciais.
Gerenciamento de Produtos: Cadastro detalhado de itens incluindo Nome, Marca, Preço e Descrição.
Consulta de Histórico: Visualização e monitoramento dos dados armazenados no banco de dados em nuvem.
Exclusão de Registros: Funcionalidade para apagar itens obsoletos ou incorretos do inventário.
Interface Customizada: Design minimalista e paleta de cores institucional aplicada via código.
Conectividade Cloud: Sincronização automática e persistência de dados via Supabase.

---

## 🛠️ Especificações Técnicas

* **Linguagem:** Python 3.x
* **Framework de GUI:** CustomTkinter
* **Banco de Dados:** Supabase / PostgreSQL
* **Versionamento:** Git & GitHub
