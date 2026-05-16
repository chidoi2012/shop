import http.server
import socketserver
import os

# Cấu hình cổng chạy trang web (Cổng 8080 rất phổ biến và an toàn)
PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Python tự động nhận diện nếu khách truy cập trang chủ không gõ gì
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Khởi tạo server kết nối máy tính của bạn với cổng mạng
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"🎉 Tuyệt vời! Server Tiệm Nhỏ Xinh đang chạy tại địa chỉ:")
    print(f"👉 Mở trình duyệt và gõ: http://localhost:{PORT}")
    print("📢 Nhấn nút Ctrl + C ở cửa sổ dòng lệnh để dừng server.")
    
    # Giữ cho server luôn chạy liên tục để phục vụ người truy cập
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server đã dừng hoạt động.")
      
