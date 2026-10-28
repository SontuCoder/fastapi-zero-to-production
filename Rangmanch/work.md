    DB_(local, any other service like NEON)
                   |
                   v
     +-----------------------------------------------+  (DB Connection, Config, Table Schemas)
     |                                               |
     v                                               v
SQLModel                                         SQLAlcamy
      |                                              |
      v<---------------------------------------------+
DB Session and Pools
          |
          v
       Pydentic(if use SQLModel, can skip it)  (Data Validation)
          |
          v
         API