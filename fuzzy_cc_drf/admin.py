from django.contrib import admin
from .models import TaskStatus, TaskPriority, TaskType, VirtualMachine, Consumption


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('description', 'criacao', 'atualizacao', 'ativo')


@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ('description', 'criacao', 'atualizacao', 'ativo')


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'criacao', 'atualizacao', 'ativo')


@admin.register(VirtualMachine)
class VirtualMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'criacao', 'atualizacao', 'ativo')


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('vm_id', 'cpu_usage','network_traffic', 'power_consumption', 'num_executed_instructions', 'execution_time', 'energy_efficiency', 'timestamp', 'criacao', 'atualizacao', 'ativo')
