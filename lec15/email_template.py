from abc import ABC, abstractmethod

class Template(ABC):
    @abstractmethod
    def generate_content(self, user: str) -> str:
        pass

class EmailSender:
    def send_email(self, email_template: Template, user: str) -> str:
        return email_template.generate_content(user)

class WelcomeEmail(Template):
    def generate_content(self, user: str) -> str:
        return f"Welcome {user}!"

class PasswordResetEmail(Template):
    def generate_content(self, user: str) -> str:
        return f"Reset password for {user}"
