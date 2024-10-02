from app.core.security import hash_password, verify_password
from app.repositories.authRepository import AuthRepository


class AuthService:
    def sign_up(name: str, phone: str, email: str, password: str):
        return AuthRepository.sign_up(name, phone, email, hash_password(password))

    def sign_in(email: str, password: str):
        user, role = AuthRepository.sign_in(email)
        if user is None or verify_password(password, user.password) == False:
            return None, None
        role = 'adm' if role != 'usr' and user.is_admin else role
        return user, role
