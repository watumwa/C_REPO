# contactbase/constants.py

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),

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
#   CONTACT CATEGORIES
# ===============================
CONTACT_CATEGORIES = [
    ('Member', 'Member'),
    ('Visitor', 'Visitor'),
    ('Donor', 'Donor'),
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
#   CSV EXPORT SETTINGS
# ===============================
CSV_HEADERS = ['Name', 'Phone', 'Email', 'Category', 'Owner']

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
