import mysql.connector

def connect_to_database():
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            database="sandaara",
            user="root",
            password="kit2025"
        )
        
        if connection.is_connected():
            print("✅ Подключение к базе данных успешно!")
            
            cursor = connection.cursor()
            
            # Запрос 1: Получаем список таблиц
            cursor.execute("SHOW TABLES;")
            print("\n📋 Таблицы в базе данных:")
            for table in cursor.fetchall():
                print(f"  - {table[0]}")
                
            # Запрос 2: Выводим товары из таблицы products
            cursor.execute("SELECT name, price FROM products;")
            print("\n📦 Товары в магазине:")
            for row in cursor.fetchall():
                print(f"  - {row[0]} (Цена: {row[1]} руб.)")
                
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as err:
        print(f"❌ Ошибка подключения: {err}")

if __name__ == "__main__":
    connect_to_database()