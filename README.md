# projeto-integrador-softex-python

## Buscador de Notícias da Paraíba (Softex / VBComunicacao)

Este repositório contém a parte **Interface** do projeto integrador “Buscador de Notícias da Paraíba”.  

---
## 📌 Descrição Geral do Sistema Desenvolvido

O sistema desenvolvido consiste em uma plataforma de gerenciamento de notícias, com controle de usuários, autenticação, validação de conteúdo e acompanhamento de métricas editoriais.

## 👤 Tela de Cadastro de Usuário
Foi implementada uma tela de cadastro, onde novos usuários podem criar uma conta informando:
-nome de usuário,
-CPF,
-tipo de usuário (jornalista ou coordenador),
-senha.

Durante o cadastro, o sistema realiza validações automáticas, como:
-confirmação correta da senha,
-verificação de CPF único,
-criação do perfil do usuário associado à conta.

## 🔐 Tela de Login
A tela de login permite que usuários cadastrados acessem o sistema de forma segura, utilizando nome de usuário e senha.
Após a autenticação:
-jornalistas são direcionados à página inicial de notícias,
-coordenadores têm acesso às funcionalidades administrativas e métricas.
Também foi configurado o logout, que encerra a sessão do usuário e redireciona corretamente para a página de login.

## 📰 Tela Inicial de Notícias (Home)
Na tela principal do sistema são exibidas as notícias cadastradas, com:

-listagem paginada,
-campo de busca por palavra-chave,
-indicação de confiabilidade da notícia (confiável, não confiável ou não avaliada).

Dependendo do tipo de usuário:
-jornalistas podem favoritar notícias,
-coordenadores podem editar notícias.

Além disso, o topo da página exibe:
-nome do usuário logado,
-tipo de usuário (jornalista ou coordenador),
-botão para acessar o perfil,
-botão de logout.

##⭐ Favoritos
Foi criada a funcionalidade de notícias favoritadas, permitindo que jornalistas:
-marquem notícias como favoritas,
-acessem uma página específica com sua lista de favoritos,
-removam notícias dos favoritos quando desejarem.

📊 Tela de Métricas (Coordenador)
A tela de métricas é restrita aos coordenadores e apresenta:
-ranking das notícias mais acessadas,
-lista de notícias pendentes de validação,
-ranking das notícias mais favoritedas pelos jornalistas,
-visualização de quais jornalistas favoritaram cada notícia.

Essa tela auxilia o coordenador na análise de engajamento e na tomada de decisão editorial.
Também foi adicionado um botão de “Voltar”, facilitando a navegação de retorno à tela principal.

##👤 Tela de Perfil
A tela de perfil permite que o usuário:
-visualize e edite seus dados pessoais,
-altere informações da conta, como nome e e-mail,
-consulte seu tipo de usuário no sistema.