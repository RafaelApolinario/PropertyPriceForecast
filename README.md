
```markdown
# 🏡 Property Price Forecast API

API para previsão de preços de imóveis, usando modelos treinados com aprendizado de máquina.

---

## 🚀 Funcionalidades

- 🔎 Previsão de preço com base em características do imóvel
- 📦 API Flask pronta para deploy
- 📊 Notebooks de análise e modelagem
- 🐳 Docker + Docker Compose integrados
- 📁 Organização limpa e modular

---

## 🗂️ Estrutura do Projeto

```
PropertyPriceForecast/
├── data/              # Dados brutos e processados
├── models/            # Modelos treinados (.pkl)
├── notebooks/         # Análises exploratórias e treinamento
├── src/api/           # Código da API Flask
├── tests/             # (Reservado para testes)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar localmente

### Com Python (Conda ou virtualenv)

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute a API Flask:

```bash
python src/api/app.py
```

3. Acesse:
- API: [http://localhost:5000](http://localhost:5000)
- Rota de teste: `/`  
- Rota de predição: `/predict` (método POST)

---

## 🐳 Como executar com Docker

1. Certifique-se de que o Docker está rodando
2. Execute:

```bash
docker-compose up --build
```

3. Acesse:
- API: [http://localhost:5000](http://localhost:5000)
- Jupyter: [http://localhost:8888](http://localhost:8888)

---

## 📥 Exemplo de Requisição `/predict`

```json
{
  "area": 5000,
  "area_per_bathroom": 2500,
  "bathrooms": 2,
  "area_per_bedroom": 1666.67,
  "airconditioning": 1,
  "parking": 1,
  "stories": 2,
  "prefarea": 1
}
```

---

## 🧠 Modelos utilizados

- `modelo_ridge.pkl` – regressão Ridge
- `modelo_rf.pkl` – Random Forest Regressor

---

## 📌 Observações

- A versão usada do `scikit-learn` no treinamento foi **1.3.0**
- Recomendado manter essa mesma versão para compatibilidade com os modelos `.pkl`

---

## 🛠️ TODOs

- [ ] Adicionar testes automatizados em `tests/`
- [ ] Melhorar documentação do notebook
- [ ] Criar pipeline para treinar novos modelos automaticamente

---

Feito com 💻 por Rafael.