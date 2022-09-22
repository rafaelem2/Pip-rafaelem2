#!/usr/bin/env python3
from datetime import date, datetime
from babel.dates import format_datetime
from dev_aberto import hello
import gettext
gettext.install('cli', localedir='locale') 


if __name__ == '__main__':
    date, name = hello()
    date_str = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    print(_('Último commit feito em:'), format_datetime(date_str), _(' por'), name)
