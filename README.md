🧴 Sistema NikBelo Luxury - Gestão de Inventário
Este repositório contém o código-fonte do sistema de gestão de produtos da NikBelo. 
O projeto adota uma arquitetura em três camadas(Front-end, Back-end e Database), garantindo escalabilidade e facilidade de manutenção.



🏛️ Arquitetura do Projeto
O software foi estruturado seguindo padrões modernos de desenvolvimento:

Camada de Apresentação (Front-end):

Desenvolvida em Python utilizando a biblioteca CustomTkinter.

Interface inspirada na estética minimalista "Branco e Dourado", proporcionando uma experiência de uso luxuosa e intuitiva.

Sistema de navegação em tela única para otimização de fluxo e memória.

Camada de Lógica de Negócios (Back-end):

Implementação de rotinas de autenticação de usuários.

Processamento e validação de dados de entrada para o inventário (Nome, Marca, Preço e Descrição).

Gerenciamento de estados da aplicação e controle de fluxo.

Camada de Persistência (Database):

Integração em tempo real com o Supabase (PostgreSQL na nuvem).

Implementação de Row Level Security (RLS), garantindo que as transações de dados ocorram em um ambiente seguro e controlado.




🚀 Funcionalidades Principais
Autenticação de Acesso: Login seguro com validação direta no servidor.

Gerenciamento de Produtos: Cadastro detalhado de itens com quatro campos técnicos obrigatórios.

Interface Customizada: Design responsivo e paleta de cores institucional aplicada via código.

Conectividade Cloud: Sincronização automática com banco de dados externo.




🛠️ Especificações Técnicas
Linguagem: Python 3.x

Framework de GUI: CustomTkinter (Efeito Moderno/Dark Mode compatível)

Banco de Dados: Supabase / PostgreSQL

Versionamento: Git & GitHub
