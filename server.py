from flask import Flask, request, jsonify

app = Flask(__name__)

# Dữ liệu mẫu về trái cây
fruits = {
    "apple": {"id": 1, "color": "red", "taste": "sweet"},
    "banana": {"id": 2, "color": "yellow", "taste": "sweet"},
    "orange": {"id": 3, "color": "orange", "taste": "tangy"}
}

# Định nghĩa route cho yêu cầu GET
@app.route('/fruit', methods=['GET', 'POST'])
def manage_fruits():
    if request.method == 'GET':
        # Lấy tên trái cây từ tham số truy vấn
        fruit_name = request.args.get('name')

        if fruit_name is None:
            return jsonify({"error": "Tên trái cây không được cung cấp."}), 400

        # Tìm kiếm thông tin của trái cây theo tên
        fruit_info = fruits.get(fruit_name.lower())

        if fruit_info:
            return jsonify(fruit_info)
        else:
            return jsonify({"error": "Không tìm thấy thông tin cho trái cây này."}), 404
    elif request.method == 'POST':
        data = request.json
        if 'name' not in data:
            return jsonify({"error": "Tên trái cây không được cung cấp."}), 400
        name = data['name'].lower()
        if name in fruits:
            return jsonify({"error": "Tên trái cây đã tồn tại."}), 400
        fruits[name] = {
            'id': len(fruits) + 1,
            'color': data.get('color', ''),
            'taste': data.get('taste', '')
        }
        return jsonify({"message": "Thêm trái cây thành công."}), 201

if __name__ == '__main__':
    app.run(debug=True)
