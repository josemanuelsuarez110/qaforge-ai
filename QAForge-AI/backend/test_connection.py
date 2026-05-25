import psycopg2

try:
    conn = psycopg2.connect(
        host="aws-1-us-west-1.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.rpgzketjnpvstunrcbxv",
        password="AngelitSecure232723",
        sslmode="require",
        connect_timeout=10
    )

    print("✅ CONECTADO A SUPABASE")

except Exception as e:
    print(f"❌ ERROR:\n{e}")
