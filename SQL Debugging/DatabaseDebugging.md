### Check for blocking
```sql
SELECT blocking_session_id, wait_type, wait_time, last_wait_type 
FROM sys.dm_exec_requests 
WHERE session_id > 50;
```

### Identify the Source (The "Who" and "Where")
``` sql
SELECT 
    session_id, 
    host_name,       -- The computer name
    program_name,    -- The app name (e.g., '.Net SqlClient', 'SQL Agent')
    login_name,      -- The user account
    status
FROM sys.dm_exec_sessions
WHERE session_id = 101; -- Replace with the current blocker ID
```

###  Check the SQL Command
``` sql
DBCC INPUTBUFFER(101); -- Replace with the current blocker ID
```

### Check what Session  is doing
''' sql
SELECT session_id, command, percent_complete, status
FROM sys.dm_exec_requests 
WHERE session_id = 101; -- Replace with the current blocker ID
'''

### Stop or Kill job
``` sql
KILL 101; -- Replace with the current blocker ID
```
