# iCalVerter
===============
**Summary**

***iCalVerter*** is a Python script, wrapped in an Apple Script Application to clean up iCal exports for import into Exchange / O365.

When completing Calendar migrations from non-exchange email hosting platforms (such as Kerio) to Office 365, we typically utilise iCal / Calendars to export an ics file from the user's current account to then be imported into the new account.

We had found that the following items produced complications with this process:

- Events with attachments failed to upload fully, with the reoccurring message of "Calendar can't save the attachment [x] to the Exchange Server"

- Events with reoccurring events often fail to upload fully.

- Events with other invited users often resend the invitations.

- Events where the user has been invited will often produce errors.

As these will produce a minimum of one pop-up per Calendar per user, these can be both irritating and time consuming to dismiss.

***iCalVerter*** will run through an exported ics file stripping out:

- Any attachments for events

- Any reoccurring events (leaving the first event in place)

- Any invitees for events

**Please Note:** Although tested internally, this tool should be considered *Beta* software and as such should only be used on ics files with a backup.

===============

**OS Compatibility:**

***iCalVerter*** has so far only been tested on OS X El Capitan (10.11.x). 


===============

**Using *iCalVerter*:**

1) Export the Calendar in question as an ics file.

2) Launch the ***iCalVerter*** Application.

3) You will be prompted to choose a file. Choose the ics file from step 1.

4) The python script will now start working on the ics file. The duration of this will depend on the size of the file.

5) Once complete, the ***iCalVerter*** Application will display a message with the name of the output file.

6) The manipulated ics file should be saved into the same location as the original and with the same name + "-outputfile.ics"



===============
**How it works:**

The ***iCalVerter*** Application's steps are all performed by the `Calendar Assistant.py` script located at iCalVerter.app/Contents/Resources/. This utilises a custom framework called [icalendar](http://icalendar.readthedocs.org/en/latest/index.html) and located at the same path.

The script will walk through the ics file, searching for each calendar event. For each event it finds, it'll set the values for the following items to blank (''):

- RRULE - Rules for reoccurring events

- ATTACH - Data for files attached to events

- ATTENDEE - Details of invited attendees and their status'

This changed version of the file is then written to disk (saved) at the same location with the value "-outputfile.ics" appended to the end.


Once complete, the python script will then use the `sed` command to remove these entries entirely from the output file.


===============
**Credits:**

- First credit to Dr. Drang, specifically for [this post](http://www.leancrew.com/all-this/2014/10/fixing-my-calendar-fixes) that gave me the bare bones of a script.

- Second credit to the team of contributors at [icalendar] (http://icalendar.readthedocs.org/en/latest/index.html) who's framework allows the ability to walk through events in an ics file and manipulate them.

- Last credit to Ivaylo 'Ivo' Mihaylov for the name and logo idea!







