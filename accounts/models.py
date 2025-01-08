from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            last_student = Student.objects.order_by('id').last()
            if last_student:
                last_id = int(last_student.student_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.student_id = f'BTR{new_id:02d}'
        super().save(*args, **kwargs)

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer_id = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.trainer_id:
            last_trainer = Trainer.objects.order_by('id').last()
            if last_trainer:
                last_id = int(last_trainer.trainer_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.trainer_id = f'MEN{new_id:02d}'
        super().save(*args, **kwargs)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.staff_id:
            last_staff = Staff.objects.order_by('id').last()
            if last_staff:
                last_id = int(last_staff.staff_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.staff_id = f'BTS{new_id:02d}'
        super().save(*args, **kwargs)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superadmin = models.BooleanField(default=False)  # True for SuperAdmin