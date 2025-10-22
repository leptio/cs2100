from typing import Optional

#class variables can access class variables using cls
#useful for configuration, alternate constructors, factory methods

class APIClient:
    base_url = 'https://api.example.com'
    timeout = 30

    @classmethod
    def configure(cls, base_url: Optional[str] = None, timeout: Optional[int] = None) -> None:
        if base_url:
            cls.base_url = base_url
        if timeout:
            cls.timeout = timeout

    @classmethod
    def reset_config(cls) -> None:
        cls.base_url = 'https://api.example.com'
        cls.timeout = 30


print(APIClient.base_url)  # https://api.example.com
print(APIClient.timeout)  # 30

APIClient.configure('new_url.com', 60)

user1 = APIClient()
print(user1.base_url)  # new_url.com
print(user1.timeout)  # 60

APIClient.reset_config()

user2 = APIClient()
print(user2.base_url)  # https://api.example.com
print(user2.timeout)  # 30
