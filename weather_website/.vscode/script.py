import sqlite3

connection = sqlite3.connect('weather_data.db')

cursor = connection.cursor()

data_entries = [
    ('Ha Noi', 'Vietnam', 22.5, 60, 5.2, 'Partly Cloudy'),
    ('Ho Chi Minh', 'Vietnam', 18.0, 75, 4.1, 'Rainy'),
    ('Can Tho', 'Vietnam', 26.3, 70, 3.6, 'Sunny'),
    ('Da Nang', 'Vietnam', 21.8, 65, 4.8, 'Cloudy'),
    ('Hai Phong', 'Vietnam', 22.5, 60, 5.2, 'Partly Cloudy'),
    ('Bac Ninh', 'Vietnam', 28.0, 50, 3.5, 'Sunny'),
    ('Bien Hoa', 'Vietnam', 18.2, 70, 6.3, 'Rainy'),
    ('Buon Ma Thuat', 'Vietnam', 30.5, 65, 4.8, 'Sunny'),
    ('Da Lat', 'Vietnam', 35.0, 40, 2.0, 'Clear Sky'),
    ('Ha Long', 'Vietnam', 21.5, 75, 5.5, 'Overcast'),
    ('Hai Duong', 'Vietnam', 29.4, 60, 4.2, 'Clear Sky'),
    ('Hue', 'Vietnam', 24.5, 55, 2.8, 'Sunny'),
    ('Long Xuyen', 'Vietnam', 31.8, 65, 5.0, 'Partly Cloudy'),
    ('Mi Tho', 'Vietnam', 27.0, 45, 3.2, 'Clear Sky'),
    ('Nha Trang', 'Vietnam', 30.1, 60, 4.4, 'Partly Cloudy'),
    ('Pleiku', 'Vietnam', 28.8, 70, 3.5, 'Humid'),
    ('Quy Nhon', 'Vietnam', 20.0, 80, 6.2, 'Foggy'),
    ('Thai Nguyen', 'Vietnam', 19.2, 65, 4.7, 'Rainy'),
    ('Thanh Hoa', 'Vietnam', 32.1, 55, 3.9, 'Clear Sky'),
    ('Thu Dau Mot', 'Vietnam', 22.5, 68, 4.0, 'Cloudy'),
    ('Viet Tri', 'Vietnam', 25.5, 60, 3.5, 'Partly Cloudy'),
    ('Vinh', 'Vietnam', 19.0, 80, 5.1, 'Drizzle'),
    ('Vung Tau', 'Vietnam', 23.5, 50, 6.0, 'Clear Sky'),
    ('Ba Ria', 'Vietnam', 24.0, 65, 4.0, 'Cloudy'),
    ('Bac Lieu', 'Vietnam', 20.8, 70, 5.5, 'Partly Cloudy'),
    ('Bac Giang', 'Vietnam', 32.5, 30, 4.2, 'Sunny'),
    ('Ben Tre', 'Vietnam', 18.8, 75, 5.0, 'Rainy'),
    ('Ca Mau', 'Vietnam', 26.0, 60, 3.8, 'Clear Sky'),
    ('Cao Lanh', 'Vietnam', 28.5, 55, 4.3, 'Humid'),
    ('Cam Pha', 'Vietnam', 17.5, 82, 5.9, 'Rainy'),
    ('Chau Doc', 'Vietnam', 29.0, 50, 4.6, 'Partly Cloudy'),
    ('Di An', 'Vietnam', 35.5, 20, 2.9, 'Clear Sky'),
    ('Dong Ha', 'Vietnam', 24.2, 65, 5.1, 'Cloudy'),
    ('Dong Hoi', 'Vietnam', 23.0, 70, 5.2, 'Sunny'),
    ('Ha Tinh', 'Vietnam', 17.3, 78, 5.7, 'Overcast'),
    ('Kon Tum', 'Vietnam', 31.0, 40, 3.6, 'Sunny'),
    ('Lang Son', 'Vietnam', 34.0, 35, 3.2, 'Clear Sky'),
    ('Lao Cai', 'Vietnam', 33.5, 45, 4.5, 'Partly Cloudy'),
    ('Mong Cai', 'Vietnam', 29.8, 50, 3.8, 'Clear Sky'),
    ('Nam Dinh', 'Vietnam', 25.2, 60, 5.1, 'Rainy'),
    ('Ninh Binh', 'Vietnam', 27.0, 65, 3.9, 'Sunny'),
    ('Phan Rang', 'Vietnam', 31.0, 70, 5.0, 'Humid'),
    ('Phan Thiet', 'Vietnam', 23.0, 55, 4.5, 'Clear Sky'),
    ('Phu Quoc', 'Vietnam', 25.5, 60, 4.3, 'Partly Cloudy'),
    ('Phu Ly', 'Vietnam', 26.0, 50, 3.8, 'Clear Sky'),
    ('Quang Ngai', 'Vietnam', 24.5, 55, 3.2, 'Sunny'),
    ('Rach Gia', 'Vietnam', 26.8, 60, 4.7, 'Cloudy'),
    ('Sa Dec', 'Vietnam', 22.0, 70, 5.1, 'Foggy'),
    ('Soc Trang', 'Vietnam', 21.5, 68, 5.3, 'Rainy'),
    ('Song Cong', 'Vietnam', 28.0, 55, 4.6, 'Clear Sky'),
    ('Son La', 'Vietnam', 31.2, 50, 4.4, 'Sunny'),
    ('Tam Ky', 'Vietnam', 30.5, 65, 5.0, 'Humid'),
    ('Tan An', 'Vietnam', 29.0, 70, 3.5, 'Overcast'),
    ('Thai Binh', 'Vietnam', 27.8, 45, 3.9, 'Clear Sky'),
    ('Tra Vinh', 'Vietnam', 19.8, 75, 4.8, 'Cloudy'),
    ('Tuy Hoa', 'Vietnam', 32.2, 40, 2.5, 'Sunny'),
    ('Tuyen Quang', 'Vietnam', 25.0, 50, 4.0, 'Clear Sky'),
    ('Uong Bi', 'Vietnam', 27.5, 55, 4.2, 'Sunny'),
    ('Vi Thanh', 'Vietnam', 30.0, 65, 4.5, 'Partly Cloudy'),
    ('Yen Bai', 'Vietnam', 28.5, 50, 4.1, 'Clear Sky'),
    ('Vinh Yen', 'Vietnam', 33.0, 35, 3.0, 'Sunny'),
    ('Bao Loc', 'Vietnam', 31.5, 60, 5.0, 'Humid'),
    ('Bac Kan', 'Vietnam', 22.5, 68, 4.3, 'Rainy'),
    ('Ben Cat', 'Vietnam', 34.0, 20, 3.5, 'Clear Sky'),
    ('Cam Ranh', 'Vietnam', 29.5, 50, 4.0, 'Partly Cloudy'),
    ('Cao Bang', 'Vietnam', 25.0, 65, 5.5, 'Overcast'),
    ('Chi Linh', 'Vietnam', 20.8, 70, 4.9, 'Rainy'),
    ('Dien Bien Phu', 'Vietnam', 19.2, 75, 5.6, 'Cloudy'),
    ('Dong Trieu', 'Vietnam', 27.0, 65, 4.1, 'Clear Sky'),
    ('Dong Xoai', 'Vietnam', 15.5, 85, 6.1, 'Drizzle'),
    ('Gia Nghia', 'Vietnam', 31.0, 55, 3.7, 'Sunny'),
    ('Go Cong', 'Vietnam', 24.5, 50, 4.6, 'Clear Sky'),
    ('Ha Giang', 'Vietnam', 30.0, 70, 4.9, 'Humid'),
    ('Ha Tien', 'Vietnam', 28.5, 45, 3.4, 'Sunny'),
    ('Hoa Binh', 'Vietnam', 22.0, 75, 5.0, 'Overcast'),
    ('Hoi An', 'Vietnam', 19.0, 72, 5.4, 'Cloudy'),
    ('Hong Ngu', 'Vietnam', 26.8, 60, 4.3, 'Partly Cloudy'),
    ('Hung Yen', 'Vietnam', 29.0, 55, 3.9, 'Sunny'),
    ('Lai Chau', 'Vietnam', 20.5, 68, 5.0, 'Rainy'),
    ('Long Khanh', 'Vietnam', 31.2, 60, 4.2, 'Humid'),
    ('Nga Bay', 'Vietnam', 21.8, 72, 5.3, 'Cloudy'),
    ('Pho Yen', 'Vietnam', 33.5, 40, 3.0, 'Clear Sky'),
    ('Phuc Yen', 'Vietnam', 35.0, 30, 2.5, 'Sunny'),
    ('Sam Son', 'Vietnam', 20.0, 70, 4.7, 'Partly Cloudy'),
    ('Tam Diep', 'Vietnam', 28.0, 50, 4.4, 'Clear Sky'),
    ('Tan Uyen', 'Vietnam', 27.5, 68, 4.2, 'Overcast'),
    ('Tay Ninh', 'Vietnam', 26.0, 70, 4.0, 'Cloudy'),
    ('Thuan An', 'Vietnam', 28.0, 75, 5.0, 'Sunny'),
    ('Tu Son', 'Vietnam', 30.5, 60, 4.8, 'Partly Cloudy'),
    ('Bangkok', 'ThaiLand', 32.0, 55, 4.5, 'Clear Sky'),
    ('Berlin', 'Germany', 31.5, 58, 4.7, 'Sunny'),
    ('Tokyo', 'Japan', 29.0, 65, 5.1, 'Humid'),
    ('Moscow', 'Russia', 28.5, 70, 4.9, 'Rainy'),
    ('Paris', 'France', 30.0, 60, 5.2, 'Partly Cloudy'),
    ('London', 'EngLand', 27.0, 68, 4.6, 'Drizzle'),
    ('Washington', 'USA', 29.5, 62, 4.4, 'Clear Sky'),
    ('Beijing', 'China', 25.0, 75, 4.3, 'Overcast')
]

connection.close()