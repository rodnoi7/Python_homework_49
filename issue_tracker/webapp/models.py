from django.db import models

# Create your models here.

class Type(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Тип задачи')
	
	def __str__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Статус задачи')

	def __str__(self):
		return self.name

class Task(models.Model):
	title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
	description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
	status = models.ForeignKey('webapp.Status', related_name='task', on_delete=models.PROTECT, verbose_name='Статус')
	type = models.ForeignKey('webapp.Type', related_name='task', on_delete=models.PROTECT, verbose_name='Тип')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

	def __str__(self):
		return self.title

