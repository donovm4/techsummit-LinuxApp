# SQL Authentication

Checklist:

- [ ] DON to let BATUHAN know that a database user is needed for SQL Authentication with connection string  
- [ ] DON to work with OREN to update lab so that database user is created on image  
- [ ] DON to confirm Linux Ubuntu application works out-the-box  

Below is the query to create the user so that the Linux Ubuntu Flask application can connect to the SQL Server and query the AdventureWorksPTO database.

```
CREATE LOGIN appuser WITH PASSWORD = 'StrongP@ssword123!';
USE AdventureWorksPTO;
CREATE USER appuser FOR LOGIN appuser;
EXEC sp_addrolemember 'db_datareader', 'appuser';  -- Optional roles
EXEC sp_addrolemember 'db_datawriter', 'appuser';
```

