import pandas as pd
import matplotlib.pyplot as plt
print("")
# Tạo một DataFrame ví dụ
data = {'Latitude': [37.7749, 34.0522, 40.7128, 41.8781],
        'Longitude': [-122.4194, -118.2437, -74.0060, -87.6298],
        'Area': [500, 800, 1000, 3000],  # Giả sử diện tích được đo bằng mét vuông
        'Price': [100000, 150000, 200000, 250000]}
df = pd.DataFrame(data)

# Sử dụng df.plot để vẽ biểu đồ giá nhà theo vĩ độ và kinh độ
plt.scatter(x=df['Longitude'], y=df['Latitude'], s=df['Area']/100, c=df['Price'], alpha=0.5, cmap='viridis')

# Đặt tên cho trục và tiêu đề
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('House Prices by Location')

# Thêm thanh màu sắc cho biểu đồ để biểu thị giá
plt.colorbar(label='Price')

# Hiển thị biểu đồ
plt.show()
