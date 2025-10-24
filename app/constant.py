# contactbase/constants.py

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

MARITAL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
]

NATIONALITY_CHOICES = [
    ('UG', 'Ugandan'),
    ('KE', 'Kenyan'),
    ('TZ', 'Tanzanian'),
    ('RW', 'Rwandan'),
    ('SS', 'South Sudanese'),
    ('OT', 'Other'),
]

# ===============================
#   USER ROLES
# ===============================
USER_ROLES = [
    ('Pastor', 'Pastor'),
    ('Member', 'Member'),
    ('Guest', 'Guest'),
    ('Admin', 'Admin'),
]

# ===============================
#   MEMBER CATEGORIES
# ===============================
MEMBER_CATEGORIES = [
    ('Member', 'Member'),
    ('Pastor', 'Pastor'),
    ('Staff', 'Staff'),

]

# ===============================
#   COMMUNICATION TYPES
# ===============================
COMMUNICATION_TYPES = [
    ('Call', 'Call'),
    ('SMS', 'SMS'),
    ('Email', 'Email'),
    ('Visit', 'Visit'),
]

# ===============================
#   EVENT TYPES
# ===============================
EVENT_TYPES = [
    ('Sunday Service', 'Sunday Service'),
    ('Fellowship', 'Fellowship'),
    ('Special Event', 'Special Event'),
    ('Meeting', 'Meeting'),
]

# ===============================
#   ATTENDANCE STATUS
# ===============================
ATTENDANCE_STATUS = [
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Late', 'Late'),
]

# ===============================
#   CSV EXPORT SETTINGS
# ===============================
MEMBER_CSV_HEADERS = ['Full Name', 'Contact 1', 'Contact 2', 'Gender', 'Email', 'Category']
COMMUNICATION_CSV_HEADERS = ['Recipient', 'Type', 'Message', 'Sent At', 'Sender']

# ===============================
#   DATABASE MAINTENANCE SETTINGS
# ===============================
WEEKLY_LOG_RETENTION_DAYS = 180   # Delete logs older than 6 months
MONTHLY_REPORT_TITLE = "Monthly Contact Growth Report"

# ===============================
#   DEFAULTS / SYSTEM CONSTANTS
# ===============================
SYSTEM_EMAIL = "noreply@churchbase.com"
BACKUP_PATH = "/var/backups/contact_base/"
