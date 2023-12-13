# saranya_anagha at saranya-anagha-MBP---9E6D4 in ~/Desktop/my_stuff/Django/core
# (Django-qj11nffP) ○ python manage.py shell
# Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from vege.models import *
# >>> querySet = Student.objects.filter(student_name__startswith = "twin")
# >>> querySet
# <QuerySet [<Student: twinkle>]>
# >>> querySet = Student.objects.filter(student_name__startswith = "A")
# >>> querySet
# <QuerySet [<Student: Alyssa Sandoval>, <Student: Andrew White>, <Student: Ashley Peterson>]>
# >>> querySet = Student.objects.filter(student_email__endswith = ".org")
# >>> querySet
# <QuerySet [<Student: Ashley Peterson>, <Student: Charles Lucas>, <Student: Donald Jensen>, <Student: Frank Spencer>, <Student: James Herrera>, <Student: Yvonne Thomas>]>
# >>> for q in querySet:
# ...     print(q.student_email)
# ... 
# cooperronald@example.org
# rhonda30@example.org
# timothyjennings@example.org
# michael30@example.org
# sandra12@example.org
# pamelasmith@example.org
# >>> querySet = Student.objects.filter(student_email__endswith = ".google")
# >>> querySet
# <QuerySet []>
# >>> querySet = Student.objects.filter(student_name__icontains = "are")
# >>> querySet
# <QuerySet [<Student: Clarence Harper>]>
# >>> querySet[0].department
# <Department: Computers>
# >>> querySet[0].student_name
# 'Clarence Harper'
# >>> querySet[0].student_id
# <StudentID: STU-0522>
# >>> querySet[0].id
# 12
# >>> querySet[0].pk
# 12
# >>> querySet[0].department.department
# 'Computers'
# >>> querySet = Student.objects.filter(department__.department = "Civil")
#   File "<console>", line 1
#     querySet = Student.objects.filter(department__.department = "Civil")
#                                       ^
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
# >>> querySet = Student.objects.filter(department__.department == "Civil")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'department__' is not defined
# >>> querySet = Student.objects.filter(department__department == "Civil")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'department__department' is not defined
# >>> querySet = Student.objects.filter(department__department = "Civil")
# >>> querySet
# <QuerySet [<Student: Brianna Jackson>, <Student: Carol Mcdonald>, <Student: Christine Rodriguez>, <Student: Courtney Savage>, <Student: Frank Spencer>, <Student: James Herrera>, <Student: Joshua Walters>, <Student: Matthew Simpson>]>
# >>> querySet = Student.objects.filter(department__department__icontains = "Civ")
# >>> querySet
# <QuerySet [<Student: Brianna Jackson>, <Student: Carol Mcdonald>, <Student: Christine Rodriguez>, <Student: Courtney Savage>, <Student: Frank Spencer>, <Student: James Herrera>, <Student: Joshua Walters>, <Student: Matthew Simpson>]>
# >>> querySet.count()
# 8
# >>> d=['Civil', 'Electronics']
# >>> querySet = Student.objects.filter(department__in = d)
# Traceback (most recent call last):
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/fields/__init__.py", line 2053, in get_prep_value
#     return int(value)
# ValueError: invalid literal for int() with base 10: 'Civil'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 1436, in filter
#     return self._filter_or_exclude(False, args, kwargs)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 1454, in _filter_or_exclude
#     clone._filter_or_exclude_inplace(negate, args, kwargs)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 1461, in _filter_or_exclude_inplace
#     self._query.add_q(Q(*args, **kwargs))
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/query.py", line 1534, in add_q
#     clause, _ = self._add_q(q_object, self.used_aliases)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/query.py", line 1565, in _add_q
#     child_clause, needed_inner = self.build_filter(
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/query.py", line 1480, in build_filter
#     condition = self.build_lookup(lookups, col, value)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/query.py", line 1307, in build_lookup
#     lookup = lookup_class(lhs, rhs)
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/lookups.py", line 27, in __init__
#     self.rhs = self.get_prep_lookup()
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/fields/related_lookups.py", line 92, in get_prep_lookup
#     self.rhs = [target_field.get_prep_value(v) for v in self.rhs]
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/fields/related_lookups.py", line 92, in <listcomp>
#     self.rhs = [target_field.get_prep_value(v) for v in self.rhs]
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/fields/__init__.py", line 2055, in get_prep_value
#     raise e.__class__(
# ValueError: Field 'id' expected a number but got 'Civil'.
# >>> querySet = Student.objects.filter(department__department__in = d)
# >>> querySet
# <QuerySet [<Student: Brianna Jackson>, <Student: Cameron Bruce>, <Student: Carol Mcdonald>, <Student: Christine Rodriguez>, <Student: Courtney Savage>, <Student: Donald Jensen>, <Student: Erika Brooks>, <Student: Frank Spencer>, <Student: James Herrera>, <Student: Joshua Walters>, <Student: Julie Sanchez>, <Student: Matthew Simpson>, <Student: Yvonne Thomas>, <Student: twinkle>]>
# >>> querySet.count()
# 14
# >>> querySet = Student.objects.exclude(department__department='Civil')
# >>> querySet.count()
# 15
# >>> len(querySet)
# 15
# >>> querySet.exists()
# True
# >>> querySet = Student.objects.all()
# >>> querySet[0:2]
# <QuerySet [<Student: Alyssa Sandoval>, <Student: Andrew White>]>
# >>> querySet.values()
# <QuerySet [{'id': 16, 'department_id': 3, 'student_id_id': 18, 'student_name': 'Alyssa Sandoval', 'student_email': 'smithkelly@example.com', 'student_age': 20, 'student_address': '8000 Bradley Canyon\nSouth Susan, OK 82439'}, {'id': 21, 'department_id': 4, 'student_id_id': 23, 'student_name': 'Andrew White', 'student_email': 'daniel48@example.net', 'student_age': 18, 'student_address': '703 Eric Mall Suite 110\nCortezmouth, IL 30948'}, {'id': 18, 'department_id': 4, 'student_id_id': 20, 'student_name': 'Ashley Peterson', 'student_email': 'cooperronald@example.org', 'student_age': 15, 'student_address': '14840 Mason Pines\nSouth Kaitlinfort, VT 04128'}, {'id': 14, 'department_id': 2, 'student_id_id': 16, 'student_name': 'Brianna Jackson', 'student_email': 'mitchell62@example.net', 'student_age': 17, 'student_address': '837 Vasquez Fall Suite 337\nNew Pamelabury, GA 42495'}, {'id': 2, 'department_id': 1, 'student_id_id': 4, 'student_name': 'Cameron Bruce', 'student_email': 'kwatson@example.com', 'student_age': 15, 'student_address': '2500 Rachel Rest\nDuanestad, MP 20230'}, {'id': 8, 'department_id': 2, 'student_id_id': 10, 'student_name': 'Carol Mcdonald', 'student_email': 'ablankenship@example.com', 'student_age': 21, 'student_address': '2546 Jeff Street\nPort Austinfurt, AL 92068'}, {'id': 23, 'department_id': 4, 'student_id_id': 25, 'student_name': 'Charles Lucas', 'student_email': 'rhonda30@example.org', 'student_age': 23, 'student_address': '75712 Gordon Ferry\nSolisfurt, NV 30992'}, {'id': 15, 'department_id': 2, 'student_id_id': 17, 'student_name': 'Christine Rodriguez', 'student_email': 'jacksonstephanie@example.net', 'student_age': 22, 'student_address': '4522 Amanda Stravenue Suite 376\nAlexischester, PA 49284'}, {'id': 12, 'department_id': 3, 'student_id_id': 14, 'student_name': 'Clarence Harper', 'student_email': 'ymartinez@example.com', 'student_age': 21, 'student_address': '288 Jessica Spring\nWest Andresborough, PR 25822'}, {'id': 6, 'department_id': 2, 'student_id_id': 8, 'student_name': 'Courtney Savage', 'student_email': 'george96@example.com', 'student_age': 17, 'student_address': '60464 Kelsey Hills Apt. 489\nSouth Elizabeth, IL 83792'}, {'id': 9, 'department_id': 4, 'student_id_id': 11, 'student_name': 'Daniel Brooks', 'student_email': 'donaldgreene@example.com', 'student_age': 17, 'student_address': '396 Diane Skyway\nLake Leslie, PA 05460'}, {'id': 10, 'department_id': 1, 'student_id_id': 12, 'student_name': 'Donald Jensen', 'student_email': 'timothyjennings@example.org', 'student_age': 25, 'student_address': '832 Brooks Port\nNorth Juliefurt, OK 73592'}, {'id': 7, 'department_id': 1, 'student_id_id': 9, 'student_name': 'Erika Brooks', 'student_email': 'joanschaefer@example.net', 'student_age': 16, 'student_address': '573 Bryan Alley\nNorth Frankberg, SD 29241'}, {'id': 22, 'department_id': 2, 'student_id_id': 24, 'student_name': 'Frank Spencer', 'student_email': 'michael30@example.org', 'student_age': 20, 'student_address': '99738 Kelly Junction Apt. 019\nSouth Aprilberg, IN 82566'}, {'id': 4, 'department_id': 4, 'student_id_id': 6, 'student_name': 'James Fischer', 'student_email': 'josephskinner@example.net', 'student_age': 18, 'student_address': '43157 Michael Cove Suite 573\nKinghaven, AR 42004'}, {'id': 20, 'department_id': 2, 'student_id_id': 22, 'student_name': 'James Herrera', 'student_email': 'sandra12@example.org', 'student_age': 21, 'student_address': '9807 Gabriella Heights\nLake Danielleview, IL 02132'}, {'id': 17, 'department_id': 2, 'student_id_id': 19, 'student_name': 'Joshua Walters', 'student_email': 'wmccarty@example.com', 'student_age': 24, 'student_address': '46373 Kimberly Glens\nParkerview, CO 62232'}, {'id': 11, 'department_id': 1, 'student_id_id': 13, 'student_name': 'Julie Sanchez', 'student_email': 'brownchristine@example.com', 'student_age': 25, 'student_address': '3095 Cuevas Streets Suite 219\nNew Adamfurt, WV 11383'}, {'id': 13, 'department_id': 4, 'student_id_id': 15, 'student_name': 'Matthew Huang', 'student_email': 'hwest@example.net', 'student_age': 22, 'student_address': '1333 Laura Parkway Apt. 294\nNorth Scott, ME 87242'}, {'id': 5, 'department_id': 2, 'student_id_id': 7, 'student_name': 'Matthew Simpson', 'student_email': 'joshua38@example.net', 'student_age': 17, 'student_address': 'USS Hampton\nFPO AA 41612'}, '...(remaining elements truncated)...']>
# >>> querySet.values()[0]
# {'id': 16, 'department_id': 3, 'student_id_id': 18, 'student_name': 'Alyssa Sandoval', 'student_email': 'smithkelly@example.com', 'student_age': 20, 'student_address': '8000 Bradley Canyon\nSouth Susan, OK 82439'}
# >>> querySet.values()[0]['student_age']
# 20
# >>> querySet.values()[0]['department']
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# KeyError: 'department'
# >>> querySet.values()[0]['department__']
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# KeyError: 'department__'
# >>> querySet.values()[0]['department__department']
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# KeyError: 'department__department'
# >>> querySet = Student.objects.all().distinct('student_age')
# >>> querySet
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 374, in __repr__
#     data = list(self[: REPR_OUTPUT_SIZE + 1])
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 380, in __len__
#     self._fetch_all()
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 1881, in _fetch_all
#     self._result_cache = list(self._iterable_class(self))
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/query.py", line 91, in __iter__
#     results = compiler.execute_sql(
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/compiler.py", line 1549, in execute_sql
#     sql, params = self.as_sql()
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/models/sql/compiler.py", line 785, in as_sql
#     distinct_result, distinct_params = self.connection.ops.distinct_sql(
#   File "/Users/saranya_anagha/.local/share/virtualenvs/Django-qj11nffP/lib/python3.9/site-packages/django/db/backends/base/operations.py", line 202, in distinct_sql
#     raise NotSupportedError(
# django.db.utils.NotSupportedError: DISTINCT ON fields is not supported by this database backend
# >>> querySet = Student.objects.all().filter(student_name__icontains='Adam')
# >>> querySet
# <QuerySet []>
# >>> querySet = Student.objects.all().filter(student_age__lte=20)
# >>> querySet.count()
# 12
# >>> querySet.reverse()
# <QuerySet [<Student: twinkle>, <Student: Matthew Simpson>, <Student: James Fischer>, <Student: Frank Spencer>, <Student: Erika Brooks>, <Student: Daniel Brooks>, <Student: Courtney Savage>, <Student: Cameron Bruce>, <Student: Brianna Jackson>, <Student: Ashley Peterson>, <Student: Andrew White>, <Student: Alyssa Sandoval>]>
# >>> querySet = Student.objects.all().values_list('id','student_name')
# >>> querySet
# <QuerySet [(16, 'Alyssa Sandoval'), (21, 'Andrew White'), (18, 'Ashley Peterson'), (14, 'Brianna Jackson'), (2, 'Cameron Bruce'), (8, 'Carol Mcdonald'), (23, 'Charles Lucas'), (15, 'Christine Rodriguez'), (12, 'Clarence Harper'), (6, 'Courtney Savage'), (9, 'Daniel Brooks'), (10, 'Donald Jensen'), (7, 'Erika Brooks'), (22, 'Frank Spencer'), (4, 'James Fischer'), (20, 'James Herrera'), (17, 'Joshua Walters'), (11, 'Julie Sanchez'), (13, 'Matthew Huang'), (5, 'Matthew Simpson'), '...(remaining elements truncated)...']>
# >>> querySet[0]
# (16, 'Alyssa Sandoval')
# >>> querySet[0][1]
# 'Alyssa Sandoval'
# >>> from django.db.models import *
# >>> from vege.models import *
# >>> Student.objects.aggregate(Avg('student_age'))
# {'student_age__avg': 19.782608695652176}
# >>> Student.objects.aggregate(Max('student_age'))
# {'student_age__max': 25}
# >>> Student.objects.aggregate(Min('student_age'))
# {'student_age__min': 15}
# >>> Student.objects.aggregate(Su,('student_age'))
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Su' is not defined
# >>> Student.objects.aggregate(Sum('student_age'))
# {'student_age__sum': 455}
# student = Student.objects.values('student_age').annotate(Count('student_age'))
# >>> student
# <QuerySet [{'student_age': 15, 'student_age__count': 2}, {'student_age': 16, 'student_age__count': 1}, {'student_age': 17, 'student_age__count': 5}, {'student_age': 18, 'student_age__count': 2}, {'student_age': 20, 'student_age__count': 2}, {'student_age': 21, 'student_age__count': 4}, {'student_age': 22, 'student_age__count': 2}, {'student_age': 23, 'student_age__count': 2}, {'student_age': 24, 'student_age__count': 1}, {'student_age': 25, 'student_age__count': 2}]>
# student = Student.objects.values('student_name').annotate(Count('student_name'))
# Each publisher, each with a count of books as a "num_books" attribute.
# >>> from django.db.models import Count
# >>> pubs = Publisher.objects.annotate(num_books=Count("book"))
# >>> pubs
# <QuerySet [<Publisher: BaloneyPress>, <Publisher: SalamiPress>, ...]>
# >>> pubs[0].num_books
# 73
# Aggregation
# >>> Book.objects.aggregate(average_price=Avg('price'))
# {'average_price': 34.35}
# Returns a dictionary containing the average price of all books in the queryset.

# Annotation
# >>> q = Book.objects.annotate(num_authors=Count('authors'))
# >>> q[0].num_authors
# 2
# >>> q[1].num_authors
# 1
# q is the queryset of books, but each book has been annotated with the number of authors.


# sort by view count
#vege = Recipe.objects.all().order_by('view_count')
# sort in descending
#vege = Recipe.objects.all().order_by('-view_count')
# get two records
#vege = Recipe.objects.all().order_by('view_count')[0:2]
# get result with confition
# Recipe.objects.filter(view_count=20)
# Recipe.objects.filter(view_count__gte=20) #spcl str in django to check greater than
# Recipe.objects.filter(view_count__gte=20)[0].view_count





# for s in Student.objects.all()[1:10]:
# ...     s.is_deleted = True
# ...     s.save()
# ... 
# >>> Student.objects.all().count()
# 91
# >>> Student.admin_objects.all().count()
# 100