from datetime import datetime, timedelta, timezone

# 서울 시간대 (UTC+9)
seoul_tz = timezone(timedelta(hours=9))

# 현재 서울 날짜
today_seoul = datetime.now(seoul_tz).date()

print(today_seoul.strftime("%Y-%m-%d"))
