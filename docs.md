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



# Feature: Delete User Account

## Description
Allow authenticated users to delete their own accounts with confirmation.

## Implementation Steps

1. **View**  
   - Added `delete_account_view` in `accounts/views.py` to handle POST request and delete the logged-in user.
   - Logs out the user before deleting their account.

2. **Template**  
   - Created `delete_account.html` template with a confirmation message and CSRF-protected form.

3. **URLs**  
   - Added `path('delete/', delete_account_view, name='delete_account')` to `accounts/urls.py`.

4. **Link**  
   - Added a link to delete account in `profile.html` (or `base.html`).

## Result
User can now navigate to `/accounts/delete/` to confirm and delete their account.

## Redirect
After deletion, the user is redirected to the register page with a success message.
