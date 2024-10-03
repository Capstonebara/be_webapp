from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Bạn có thể thay bằng URL của các DB khác như PostgreSQL

# Kết nối đồng bộ (nếu không dùng async)
engine = create_engine(DATABASE_URL)

# Sử dụng MetaData để quản lý các bảng
metadata = MetaData()

# Base class để tạo các mô hình (models)
Base = declarative_base()

# Session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)