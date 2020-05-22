from flask_restful import Resource, reqparse
from models.users import UserModel


class RegisterUsers(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='insert username'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Enter a password'
                        )

    def post(self):
        data = RegisterUsers.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "username already taken"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User registered successfully"}, 201  # created
