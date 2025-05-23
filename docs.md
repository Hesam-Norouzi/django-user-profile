### ✅ Feature: Password Change

**Description:**  
Added support for authenticated users to securely change their passwords using Django's built-in views.

**Added URLs:**
- `/accounts/password_change/` — password change form
- `/accounts/password_change/done/` — success confirmation page

**Updated Files:**
- `accounts/urls.py` — registered password change views
- `accounts/templates/accounts/password_change.html` — password change form template
- `accounts/templates/accounts/password_change_done.html` — success message template
- `accounts/templates/base.html` — added link to "Change Password"

**Dependencies Used:**
- `PasswordChangeView` and `PasswordChangeDoneView` from `django.contrib.auth.views`

**Result:**  
Authenticated users can now change their password and get redirected to a confirmation page upon success.
