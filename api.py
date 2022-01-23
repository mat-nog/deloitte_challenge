from api_db import *

# Endopoint para mostrar todos os membros da equipe
@app.route('/team', methods=['GET'])
def get_members():
    return jsonify({'Members': Team.get_all_members()})

# Endopoint para mostrar algum membro especifico
@app.route('/team/<int:id>', methods=['GET'])
def get_members_by_id(id):
    return_value = Team.get_member(id)
    return jsonify(return_value)

# Endopoint para adcionar um membro a equipe
@app.route('/team', methods=['POST'])
def add_member():
    request_data = request.get_json()  
    Team.add_member(request_data["name"], request_data["register"], request_data["role"])
    response = Response("Member added", 201, mimetype='application/json')
    return response

# Endopoint para atualizar algum membro da equipe
@app.route('/team/<int:id>', methods=['PUT'])
def update_member(id):
    request_data = request.get_json()
    Team.update_member(id, request_data['name'], request_data['register'], request_data['role'])
    response = Response("Member Updated", status=200, mimetype='application/json')
    return response

# Endopoint para excluir algum membro da equipe
@app.route('/team/<int:id>', methods=['DELETE'])
def remove_member(id):
    Team.delete_member(id)
    response = Response("Member Deleted", status=200, mimetype='application/json')
    return response

# Endopoint para mostrar todos os serviços
@app.route('/services', methods=['GET'])
def get_services():
    return jsonify({'Services': Services.get_all_services()})

# Endopoint para mostrar algum serviço especifico
@app.route('/services/<int:id>', methods=['GET'])
def get_service_by_id(id):
    return_value = Services.get_service(id)
    return jsonify(return_value)

# Endopoint para adcionar um serviço
@app.route('/services', methods=['POST'])
def add_service():
    request_data = request.get_json()
    Services.add_service(request_data["name"], request_data["duration"], request_data["price"])
    response = Response("Service added", 201, mimetype='application/json')
    return response

# Endopoint para atualizar algum serviço
@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    request_data = request.get_json()
    Services.update_service(id, request_data['name'], request_data['duraton'], request_data['price'])
    response = Response("Service Updated", status=200, mimetype='application/json')
    return response

# Endopoint para excluir algum serviço
@app.route('/services/<int:id>', methods=['DELETE'])
def remove_service(id):
    Services.delete_service(id)
    response = Response("Service Deleted", status=200, mimetype='application/json')
    return response

# Endopoint para mostrar todos os posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'Posts': Posts.get_all_posts()})

# Endopoint para mostrar algum post especifico
@app.route('/posts/<int:id>', methods=['GET'])
def get_post_by_id(id):
    return_value = Posts.get_service(id)
    return jsonify(return_value)

# Endopoint para adcionar um post
@app.route('/posts', methods=['POST'])
def add_post():
    request_data = request.get_json() 
    Posts.add_post(request_data["name"], request_data["email"], request_data["date"], request_data["content"])
    response = Response("Post added", 201, mimetype='application/json')
    return response

# Endopoint para atualizar algum post
@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    request_data = request.get_json()
    Posts.update_post(id, request_data['date'], request_data['content'])
    response = Response("Post Updated", status=200, mimetype='application/json')
    return response

# Endopoint para excluir algum post
@app.route('/posts/<int:id>', methods=['DELETE'])
def remove_post(id):
    Posts.delete_post(id)
    response = Response("Post Deleted", status=200, mimetype='application/json')
    return response

# Configura a port na qual a aplicação estara ligada para ser executada
if __name__ == "__main__":
    app.run(port=5000, debug=True)