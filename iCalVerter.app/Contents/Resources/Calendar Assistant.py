#!/usr/bin/python

import imp
import sys
from datetime import timedelta
import subprocess
from icalendar import Calendar
import os
from os.path import basename

for ics in sys.argv[1:]:
  # Open the ics file and extract the events
  cal = Calendar.from_ical(open(ics).read())
  for component in cal.walk():
      ics_old = os.path.splitext(ics)[0]
      out_file = ics_old + "-outputfile.ics"
  # Erase the event's RRULE, ATTACH and ATTENDEE items
      component['RRULE'] = ''
      component['ATTACH'] = ''  
      component['attendee'] = ['']
      component['ORGANIZER'] = ''  

  # Write the changes back to the original file.
  f = open(out_file, 'w')
  f.write(cal.to_ical())
  f.close()
  
  
# Use sed to remove the placeholder values
  subprocess.call(['sed', '-i', '', '/RRULE/d', out_file ])
  subprocess.call(['sed', '-i', '', '/ATTENDEE/d', out_file ])
  subprocess.call(['sed', '-i', '', '/ATTACH/d', out_file ])
  subprocess.call(['sed', '-i', '', '/ORGANIZER/d', out_file ])  
  