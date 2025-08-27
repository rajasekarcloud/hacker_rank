from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
stocks = {
    'AAPL': 192.5,
    'GOOG': 134.2,
    'TSLA': 242.1
}

portfolio = {}

@app.route('/stocks', methods=['GET'])
def view_stocks():
    return jsonify(stocks)

@app.route('/buy', methods=['POST'])
def buy_stock():
    data = request.json
    symbol = data.get('symbol')
    quantity = data.get('quantity')

    if symbol not in stocks:
        return jsonify({'error': 'Invalid stock symbol'}), 400

    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    return jsonify({'message': f'Bought {quantity} shares of {symbol}'})

@app.route('/portfolio', methods=['GET'])
def view_portfolio():
    total_value = sum(stocks[symbol] * qty for symbol, qty in portfolio.items())
    return jsonify({
        'holdings': portfolio,
        'total_value': total_value
    })

if __name__ == '__main__':
    app.run(debug=True)