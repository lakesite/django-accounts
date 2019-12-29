# rationale #

So, why create django-accounts?

1. Most Django projects that aren't pure APIs will require account templates.
2. We should standardize them and make the generic templates look good for our 
   projects.
3. We should document how we'll override them.
4. We've standardized on a custom user model, django-emailuser, and require 
   logins that use emails instead of usernames.
