# Xquisite AI CRUD API

Sebuah proyek FastAPI yang menyediakan CRUD (Create, Read, Update, Delete) untuk mengelola kategori dan item dalam sebuah database menggunakan SQLAlchemy.

## 🚀 Fitur
- **Manajemen Kategori**: Tambah, baca, perbarui, dan hapus kategori.
- **Manajemen Item**: Tambah, baca, perbarui, dan hapus item yang terkait dengan kategori.
- **Database Management**: Menggunakan SQLite sebagai database default.
- **Pydantic Validation**: Memvalidasi input dan output data.

## 🛠 Teknologi yang Digunakan
- **FastAPI** - Framework Python untuk API yang cepat dan mudah digunakan.
- **SQLAlchemy** - ORM untuk mengelola database.
- **Pydantic** - Validasi data dengan Python.
- **Uvicorn** - Server ASGI untuk menjalankan aplikasi.

## 📦 Instalasi
### 1. Clone Repository
```bash
git clone https://github.com/username/xquisite_ai.git
cd xquisite_ai
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Instal Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Database Migration (Opsional jika menggunakan SQLite)
```bash
alembic upgrade head
```

### 5. Jalankan Server
```bash
uvicorn main:app --reload
```

Aplikasi akan berjalan di `http://127.0.0.1:8000`

## 📖 API Endpoints
### **Kategori**
| Method | Endpoint       | Deskripsi                  |
|--------|---------------|----------------------------|
| `POST` | `/categories/` | Tambah kategori baru       |
| `GET`  | `/categories/` | Ambil semua kategori       |
| `GET`  | `/categories/{id}` | Ambil kategori berdasarkan ID |
| `PUT`  | `/categories/{id}` | Perbarui kategori         |
| `DELETE` | `/categories/{id}` | Hapus kategori            |

### **Item**
| Method | Endpoint       | Deskripsi                  |
|--------|---------------|----------------------------|
| `POST` | `/items/`      | Tambah item baru           |
| `GET`  | `/items/`      | Ambil semua item           |
| `GET`  | `/items/{id}`  | Ambil item berdasarkan ID  |
| `PUT`  | `/items/{id}`  | Perbarui item              |
| `DELETE` | `/items/{id}` | Hapus item                 |

## 📌 Cara Menggunakan
1. **Buka Dokumentasi API**: FastAPI menyediakan dokumentasi otomatis yang bisa diakses di:
   - `http://127.0.0.1:8000/docs` (Swagger UI)
   - `http://127.0.0.1:8000/redoc` (ReDoc UI)

2. **Gunakan Postman atau cURL** untuk menguji endpoint.

## ❗ Troubleshooting
- **Database Locked**: Pastikan tidak ada proses lain yang menggunakan `test.db`. Jika terjadi error, coba hapus database:
  ```bash
  rm test.db  # Linux/Mac
  del test.db  # Windows
  ```
- **Error 500 (Internal Server Error)**: Pastikan model database memiliki hubungan `ForeignKey` yang benar.




