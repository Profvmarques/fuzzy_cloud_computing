from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class VirtualMachine(Base):
    id = models.CharField(max_length=40, primary_key=True, unique=True, blank=False)

    class Meta:
        verbose_name = 'Virtual Machine'
        verbose_name_plural = 'Virtual Machines'
        ordering = ['id']

    def __str__(self):
        return self.id


class TaskPriority(Base):
    description = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = 'Task Priority'
        verbose_name_plural = 'Tasks priorities'
        ordering = ['description']

    def __str__(self):
        return self.description


class TaskStatus(Base):
    description = models.CharField(max_length=35, blank=False)

    class Meta:
        verbose_name = 'Task Status'
        verbose_name_plural = 'Tasks Status'
        ordering = ['description']

    def __str__(self):
        return self.description


class TaskType(Base):
    description = models.CharField(max_length=35, blank=False)

    class Meta:
        verbose_name = 'Task Type'
        verbose_name_plural = 'Tasks Types'
        ordering = ['description']

    def __str__(self):
        return self.description


class Consumption(Base):
    vm_id = models.ForeignKey(VirtualMachine, related_name='virtual_machines', on_delete=models.CASCADE)
    tp_id = models.ForeignKey(TaskPriority, related_name='task_priorities', on_delete=models.CASCADE)
    tt_id = models.ForeignKey(TaskType, related_name='task_types', on_delete=models.CASCADE)
    ts_id = models.ForeignKey(TaskStatus, related_name='task_statuses', on_delete=models.CASCADE)
    cpu_usage = models.DecimalField(max_digits=8, decimal_places=6)
    memory_usage = models.DecimalField(max_digits=8, decimal_places=6)
    network_traffic = models.DecimalField(max_digits=9, decimal_places=6)
    power_consumption = models.DecimalField(max_digits=9, decimal_places=6)
    num_executed_instructions = models.DecimalField(max_digits=10, decimal_places=1)
    execution_time = models.DecimalField(max_digits=8, decimal_places=6)
    energy_efficiency = models.DecimalField(max_digits=7, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = 'Consumption'
        verbose_name_plural = 'Consumptions'
        ordering = ['vm_id']

    def __str__(self):
        return self.vm_id


