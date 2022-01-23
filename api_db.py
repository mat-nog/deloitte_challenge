from settings import *
import json

db = SQLAlchemy(app)

# Classe com metodos para manipular a tabela com os membros da equipe
class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    register = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def json(self):
            return {'id': self.id, 'name': self.name,
                    'register': self.register, 'role': self.role}

    def add_member(_name, _register, _role):
        new_member = Team(name=_name, register=_register, role=_role)
        db.session.add(new_member)
        db.session.commit()

    def get_all_members():
        return [Team.json(member) for member in Team.query.all()]

    def get_member(_id):
        return [Team.json(Team.query.filter_by(id=_id).first())]


    def update_member(_id, _name, _register, _role):
        member_to_update = Team.query.filter_by(id=_id).first()
        member_to_update.name = _name
        member_to_update.register = _register
        member_to_update.role = _role
        db.session.commit()

    def delete_member(_id):
        Team.query.filter_by(id=_id).delete()
        db.session.commit()

# Classe com metodos para manipular a tabela com os serviços
class Services(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def json(self):
            return {'id': self.id, 'name': self.name,
                    'duration': self.duration, 'price': self.price}

    def add_service(_name, _duration, _price):
        new_service = Services(name=_name, duration=_duration, price=_price)
        db.session.add(new_service)
        db.session.commit()

    def get_all_services():
        return [Services.json(service) for service in Services.query.all()]

    def get_service(_id):
        return [Services.json(Services.query.filter_by(id=_id).first())]

    def update_service(_id, _name, _duration, _price):
        member_to_update = Services.query.filter_by(id=_id).first()
        member_to_update.name = _name
        member_to_update.duration = _duration
        member_to_update.price = _price
        db.session.commit()

    def delete_service(_id):
        Services.query.filter_by(id=_id).delete()
        db.session.commit()

# Classe com metodos para manipular a tabela com os posts
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(256), nullable=False)

    def json(self):
            return {'id': self.id, 'name': self.name,
                    'email': self.email, 'date': self.date,
                    'content': self.content}

    def add_post(_name, _email, _date, _content):
        new_post = Posts(name=_name, email=_email, date=_date, content= _content)
        db.session.add(new_post)
        db.session.commit()

    def get_all_posts():
        return [Posts.json(post) for post in Posts.query.all()]

    def get_post(_id):
        return [Posts.json(Posts.query.filter_by(id=_id).first())]

    def update_post(_id, _date, _content):
        post_to_update = Posts.query.filter_by(id=_id).first()
        post_to_update.date = _date
        post_to_update.content = _content
        db.session.commit()

    def delete_post(_id):
        Posts.query.filter_by(id=_id).delete()
        db.session.commit()

# Cria o DB e preenche com alguns dados fantasia
if not database_exists('sqlite:///database.db'):
    db.create_all()
    Services.add_service('Desenvolvimento de API', 80, 20000)
    Services.add_service('Case para code challenge', 60, 15000)
    Services.add_service('API para site de servicos', 120, 24000)
    Posts.add_post('Lucas', 'lucas@email.com.br', '23/01/2022', 'Empresa muito profissional, realizaram o serviço foi muito bem feito e rapidamente')
    Posts.add_post('Joana', 'joana@email.com.br', '17/01/2022', 'Rapidos e eficientes, recomendo')
    Posts.add_post('Maria', 'maria@email.com.br', '04/11/2021', 'Tive uma otima experiencia, voltarei a fazer mais negocios com eles')
    Team.add_member('Matheus', 135598, 'Desenvolvedor')
    Team.add_member('Luisa', 15442, 'Gerente de Projetos')
    Team.add_member('Jorge', 1789, 'Diretor')
    db.session.commit()