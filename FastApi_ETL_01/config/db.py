from sqlalchemy import create_engine, MetaData
import pymysql

engine = create_engine("mysql+pymsyql://root:1234@localhost:3306/etl_proyecto1")

meta = MetaData()

conn = engine.connect()