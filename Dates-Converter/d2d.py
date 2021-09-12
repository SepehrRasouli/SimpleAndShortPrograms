# Very Simple Program To Convert Gregorian Date To Jalali And Vice Versa.
import argparse as arg
import difflib as differ
from dateutil.parser import *
from persiantools.jdatetime import JalaliDate
from dateparser.calendars.jalali import JalaliCalendar
parser = arg.ArgumentParser()
parser.add_argument("-g2j",help="Gregorian To Jalali")
parser.add_argument("-j2g",help="Jalili To Gregorian")
parser.add_argument("-v",help="",action="store_true")
args= parser.parse_args()

if args.g2j:
    Date = parse(args.g2j)
    print(f"Gregorian => {Date} " + f"\n{Date.strftime('%A %-dth Of %B Year %Y')}"*args.v) 
    Jalali = JalaliDate.to_jalali(Date)
    print(f"\nJalili => {Jalali}" + f" \n{Jalali.ctime()}"*args.v)

if args.j2g:
    Date = JalaliCalendar(args.j2g).get_date()
    Jalali = JalaliDate.to_jalali(Date.date_obj)
    print("\nJalali => {Jalali}" + f" \n{Jalali.ctime()}"*args.v)
    print("\nGregorian => {Date}" + f" \n{Date.date_obj.strftime('%A %-dth Of %B Year %Y')}")

