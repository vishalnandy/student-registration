import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

conn = psycopg2.connect(
    dbname="postgres",  # or your specific DB name
    user="postgres.tvlobiffdkivwwpyolwi",
    password="Vishal1nand@",
    host="aws-0-ap-south-1.pooler.supabase.com",
    port="6543",
    sslmode='require'
)

print("✅ Connected successfully!")
conn.close()
