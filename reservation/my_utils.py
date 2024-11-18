from datetime import datetime, date
from django.core.exceptions import ValidationError


def check_clashes(model, room, start, end):
    '''Check for clashed if the time pick doesn't fall among the already picked time.
    Get all the times in the DB (start and end) check then with the new time if no clash exist they should be able to book.

    Case:
    The new booking's start date is before the existing booking's end date.
    The new booking's end date is after the existing booking's start date.

          unique_together = ('customer', 'room', 'check_in_date', 'check_out_date')
    '''

    room_bookings = model.objects.filter(room_id=room).values_list(
        'check_in_date', 'check_out_date')

    clash_box = []
    for (check_in_date, check_out_date) in room_bookings:
        # 15 - 17, 16-18 ,
        if start < check_out_date and end > check_in_date:
            clash_box.append((check_in_date, check_out_date))
            print(
                f'$$$$$$$$$$ A clash exists between {start} - {end} and a booked period of  {check_in_date} - {check_out_date} !!!')

        if clash_box:
            raise ValidationError(
                f' A clash exists between {start} - {end} and a booked period of  {check_in_date} - {check_out_date} !!!')

    return f'You can pick that time {start} - {end}'
