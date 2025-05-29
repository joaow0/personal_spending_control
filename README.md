# 💰 Personal Expense Tracker | Controle de Gastos Pessoais

A simple Django project to track personal expenses. You can register your expenses with a description, amount, category, and date. The application displays the expenses in a table for easy visualization.

Um projeto simples em Django para controle de despesas pessoais. Você pode cadastrar suas despesas com descrição, valor, categoria e data. A aplicação exibe os gastos em uma tabela para fácil visualização.

---

## 🚀 Features | Funcionalidades

- ✅ Add expenses with:
  - Description | Descrição
  - Value | Valor
  - Category | Categoria
  - Date | Data
- ✅ Filter expenses by category *(optional)*
- ✅ Responsive layout with Bootstrap
- ✅ Clean and simple interface

---

## 🛠️ Technologies | Tecnologias

- Python 🐍
- Django 🌐
- HTML + CSS 🎨
- Bootstrap 💎

---

## 💻 Installation | Instalação

### Requirements | Requisitos

- Python 3.x
- Virtualenv *(recommended)*

### ▶️ Running the project | Rodando o projeto

```bash
# Clone the repository
git clone https://github.com/joaow0/personal_spending_control

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows


venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate


# Run migrations
python manage.py migrate

# Run the server
python manage.py runserver
