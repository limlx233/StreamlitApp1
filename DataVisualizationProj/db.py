import os
import streamlit as st
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 定义数据库路径和连接 URL
db_path =  st.secrets["database"]["db_path"]
# db_path = "./user_data.db"

# 检查数据库文件路径是否存在，如果不存在则创建
# if not os.path.exists(os.path.dirname(db_path)):
#     os.makedirs(os.path.dirname(db_path))

SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"
Base = declarative_base()

# 定义模型
class UserInfo(Base):
    __tablename__ = "userinfo"
    
    usrname = Column(String, primary_key=True) # 添加 nullable=False 确保不允许为 null
    usrpwd = Column(String, nullable=False) # 添加 nullable=False 确保不允许为 null

# 创建 SQLite 数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 尝试连接数据库并创建表
try:
    with engine.connect() as connection:
        # 确保表存在，实际创建
        Base.metadata.create_all(bind=engine)
        print("Successfully connected to the database")
except OperationalError as e:
    print(f"Error connecting to the database: {e}")

# 创建会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)