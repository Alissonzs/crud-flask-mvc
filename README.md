# CRUD de Usuários com Flask + MySQL

Este projeto é uma aplicação web simples desenvolvida com **Python**, **Flask**, **MySQL** e **Bootstrap**, que implementa um CRUD completo (Create, Read, Update, Delete) de usuários.

## 📌 Funcionalidades

- ✅ Cadastrar novo usuário  
- ✅ Listar usuários cadastrados  
- ✅ Editar informações do usuário  
- ✅ Excluir usuário

## 🧩 Tecnologias Utilizadas

- **Back-end:** Python + Flask  
- **Banco de dados:** MySQL  
- **Front-end:** HTML + Bootstrap  
- **Padrão de Projeto:** MVC (Model-View-Controller)

## ⚙️ Como rodar o projeto

1. Clone este repositório ou baixe os arquivos
2. Crie um banco de dados MySQL chamado `crud_usuarios`
3. Execute o seguinte script SQL no banco:

```sql
CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  senha VARCHAR(100)
);
