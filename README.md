# projChatPyDjango
Este projeto consiste na criação de um backend robusto utilizando Django e Django Rest Framework para dar suporte a um aplicativo de comunicação entre pessoas.

## Funcionalidades

- Cadastro de usuários personalizado.
- Sistema de autenticação e gerenciamento de usuários.
- Suporte a salas de chat com WebSocket.
- Comunicação em tempo real utilizando Django Channels e Redis.

---

## Tecnologias Utilizadas

### Backend
- **Python**: Linguagem principal do projeto.
- **Django**: Framework web para construção do backend.
- **Django Channels**: Para implementar comunicação em tempo real via WebSocket.
- **Redis**: Utilizado como backend para o Channels Layer.

### Frontend
- **HTML/JavaScript**: Para testes de funcionalidade e interface simples de chat.

---

## Configuração do Projeto

### Pré-requisitos

1. **Python 3.8+**: [Download aqui](https://www.python.org/downloads/).
2. **Redis**: Certifique-se de que o Redis está instalado e rodando na porta padrão (6379). Você pode instalá-lo [aqui](https://redis.io/download).

---

### Passos de Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chat-py-django.git
   cd chat-py-django
