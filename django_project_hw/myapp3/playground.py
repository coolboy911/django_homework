from datetime import datetime, timedelta

now_date = datetime.now()
print(f'{now_date.isoformat() = }')

start_date = now_date - timedelta(days=365)
print(f'{start_date.isoformat() = }')
