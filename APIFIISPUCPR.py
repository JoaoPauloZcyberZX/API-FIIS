from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='static')

# ✅ Coloque seu token da BRAPI aqui (cadastre-se em https://brapi.dev)
TOKEN = "48ifJA1gcFqC68DkECskTk"

# Lista dos fundos com maiores dividendos
TOP_TICKERS = ["DEVA11", "URPR11", "KIVO11", "CACR11", "LIFE11",
               "AIEC11", "BLMG11", "KORE11", "TGAR11", "BPML11"]

@app.route('/api/fiis')
def get_fiis_data():
    results = []
    for ticker in TOP_TICKERS:
        try:
            response = requests.get(
                f"https://brapi.dev/api/quote/{ticker}?fundamental=true&dividends=true&token={TOKEN}"
            )
            data = response.json().get("results", [{}])[0]
            print(f"Resposta API para {ticker}: {data}")  # Debug
            results.append({
                "ticker": ticker,
                "price": data.get("regularMarketPrice"),
                "dividend_yield": data.get("dividendYield"),
                "last_dividend": data.get("lastDividend"),
                "last_dividend_date": data.get("lastDividendDate")
            })
        except Exception as e:
            print(f"Erro ao buscar {ticker}: {e}")
    return jsonify(results)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')  # Corrigido aqui!

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
