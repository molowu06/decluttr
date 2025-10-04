The Backend

So FAR:
- setup with gmail api integration, so once the user logins we fetch all of 
their emails from the last month and organize them in the most popular way
with details associated with each sender. Then we can give them the option 
to first unsubscribe.

TODO:
- we need dynamic token refreshing for the oauth so we can continuously access
their info
- let the user provide certain info they'd like to see in emails, then list them as
starred automatically if a subject line with that phrase shows up

1. User Authentication (Google OAuth)
- Handles the google oauth flow securely
- get access tokens to fetch user gmail data
- refresh tokens if needded to keep access alive during a sesh

2. Gmail API Integration
- Use Google's Gmail API to:
    -> list user emails (filtered to promotional / newsletters)
    -> Fetch full email details (headers like From, Subject, List-Unsubscribe)

3. Serve Data to Frontend
- Craete API ENdpoints your frontend can call to:
    - get list of senders + email counts
    - get unsub links per sender
    - save user prefs

4. Storage (Optional)

5. Security -> Keep OAUth tokens secret on the servert