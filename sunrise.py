from datetime import datetime

sunrise_timestamp = 1730326244

sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp)
print("Sunrise time:", sunrise_time.strftime('%Y-%m-%d %H:%M:%S UTC'))
