from database import engine, Base

# Importar modelos
from models.user import User
# importa aquí tus otros modelos
# from models.prompt import Prompt

print("🚀 Creando tablas...")

Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente!")
