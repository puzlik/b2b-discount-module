=====
B2B Discount Module
=====

Discount module is a simple Django app to conduct Web-based b2b discount module.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "discount_module" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'discount_module',
    )

2. Include the discount_module URLconf in your project urls.py like this::

    url(r'^discount/', include('discount_module.urls')),

3. Run `python manage.py migrate` to create the discount_module models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a discount_module (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/discount/ to participate in the discount.
