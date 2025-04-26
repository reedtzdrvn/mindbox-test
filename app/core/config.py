import os
from dotenv import load_dotenv


load_dotenv(override=True)

POSTGRESQL = 'postgresql'
SQLITE = 'sqlite'

class Config:
    DB_TYPE: str = os.getenv('DB_TYPE', SQLITE)

    # PostgreSQL
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "products_db")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    DATABASE_URL: str = os.getenv('DATABASE_URL')
    

    def get_database_url(self) -> str:
        postgres_host = self.POSTGRES_HOST
        if os.getenv('DOCKER_ENV') == 'true':
            postgres_host = 'db'
            
        if self.DATABASE_URL:
            if os.getenv('DOCKER_ENV') == 'true' and 'localhost' in self.DATABASE_URL:
                return self.DATABASE_URL.replace('localhost', 'db')
            return self.DATABASE_URL
        
        if self.DB_TYPE == POSTGRESQL:
            return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{postgres_host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
        raise ValueError(f"Unsupported DB_TYPE: {self.DB_TYPE}")
        
config = Config()