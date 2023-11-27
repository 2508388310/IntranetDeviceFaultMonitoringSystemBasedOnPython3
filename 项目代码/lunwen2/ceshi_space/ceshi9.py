import os
ThreadID = os.getpid() & 0xFF
print(ThreadID)
print(os.getpid())