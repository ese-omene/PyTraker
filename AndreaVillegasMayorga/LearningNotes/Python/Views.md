# Write Views that actually do something
Each view is responsible for one of 2 things:
- returning an HttpResponse object containing the content for the requested page
- raising an exception such as Http404.
The rest is up to you.

Views can:
- read records from a database
- can use a template system such as Django’s – or a third-party Python template system
-  **It can generate a PDF**
-  Output XML
- create a ZIP file on the fly

**All Django wants is that HttpResponse. Or an exception.**


