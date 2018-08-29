from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=30,unique = True)
    faculty = models.CharField(max_length=30)
    def n_students(self):
        return self.all_students.count()

    def __str__(self):
        return self.name


class StudentMarks(models.Model):
    student_name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject,to_field = 'name',db_column="subject",
                                                    related_name= 'all_students',
                                                    on_delete=models.CASCADE)
    marks = models.IntegerField()
