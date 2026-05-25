import psycopg2

try:
    conn = psycopg2.connect(
        host="db.rpgzketjnpvstunrcbxv.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="AngelitSecure232723",
        sslmode="require",
        connect_timeout=15
    )

    print("✅ CONEXIÓN DIRECTA EXITOSA")

except Exception as e:
    print(f"❌ ERROR:\n{e}")
