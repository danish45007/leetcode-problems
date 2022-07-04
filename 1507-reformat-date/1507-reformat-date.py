class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        date = date.split(' ')
        day = date[0]
        day = day[:-2] if len(day[:-2]) == 2 else '0' + day[:-2] 
        month = months[date[1]] if months[date[1]] >= 10 else '0' + str(months[date[1]])
        year = date[2]
        return f'{year}-{(month)}-{day}'
        