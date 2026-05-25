from database import engine, Base

print("🚀 Creando tablas...")

Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente!")