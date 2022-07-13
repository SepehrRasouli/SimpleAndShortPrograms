# Very Simple Program To Convert Gregorian Date To Jalali And Vice Versa.
import argparse as arg
from dateutil.parser import parse
from persiantools.jdatetime import JalaliDate
from dateparser.calendars.jalali import JalaliCalendar
parser = arg.ArgumentParser()
parser.add_argument("-g2j", help="Gregorian To Jalali")
parser.add_argument("-j2g", help="Jalili To Gregorian")
parser.add_argument("-v", help="", action="store_true")
args = parser.parse_args()

if args.g2j:
    Gregorian = parse(args.g2j)  # Parses Arguments
    print(f"Gregorian => {Gregorian }" +
          f"\n{Gregorian .strftime('%A, %dth Of %B, Year %Y')}"*args.v)
    Jalali = JalaliDate.to_jalali(Gregorian)
    print(f"\nJalili => {Jalali}" + f" \n{Jalali.ctime()}"*args.v)

if args.j2g:
    Gregorian = JalaliCalendar(args.j2g).get_date()
    Jalali = JalaliDate.to_jalali(Gregorian.date_obj)
    print(f"\nJalali => {Jalali}" + f" \n{Jalali.ctime()}"*args.v)
    print(f"\nGregorian => {Gregorian.date_obj}" +
          f"\n{Gregorian.date_obj.strftime('%A, %dth Of %B, Year %Y')}")
