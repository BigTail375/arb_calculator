from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/page', methods=['POST'])
def get_page():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract 'number' from the request data
        page_number = data.get('page')

        # Check if 'number' is an integer
        if page_number is None:
            return jsonify({'error': 'No number provided'}), 400
        if not isinstance(page_number, int):
            return jsonify({'error': 'The number must be an integer'}), 400

        # Return the number as part of the response
        return jsonify({'number': page_number}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
