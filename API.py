from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
blogs = []

@app.route('/api/blogs', methods=['GET'])
def get_all_blogs():
    return jsonify(blogs), 200

@app.route('/api/blogs/<int:blog_id>', methods=['GET'])
def get_blog_by_id(blog_id):
    for blog in blogs:
        if blog['id'] == blog_id:
            return jsonify(blog), 200
    return jsonify({'message': 'Blog not found'}), 404

@app.route('/api/blogs', methods=['POST'])
def post_blog():
    new_blog = {
        'id': len(blogs) + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'category': request.json['category']
    }
    blogs.append(new_blog)
    return jsonify(new_blog), 201

@app.route('/api/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    for blog in blogs:
        if blog['id'] == blog_id:
            blog['title'] = request.json.get('title', blog['title'])
            blog['description'] = request.json.get('description', blog['description'])
            blog['category'] = request.json.get('category', blog['category'])
            return jsonify(blog), 200
    return jsonify({'message': 'Blog not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
