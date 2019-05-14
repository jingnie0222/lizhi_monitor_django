from django.db import models


# Create your models here.
# '''
# class Qps(models.Model):
#     create_time = models.CharField(max_length=50, default="")
#     start_time = models.CharField(max_length=50, default="")
#     end_time = models.CharField(max_length=50, default="")
#     user = models.CharField(max_length=50)
#     status = models.IntegerField(default=0)
#     step = models.IntegerField(default=-1)
#     testitem = models.IntegerField(default=0)
#     newdataip = models.CharField(max_length=500, default="")
#     newdatauser = models.CharField(max_length=500, default="")
#     newdatapassw = models.CharField(max_length=500, default="")
#     newdatapath = models.CharField(max_length=500, default="")
#     newdata_topath = models.CharField(max_length=500, default="")
#     newconfip = models.CharField(max_length=500, default="")
#     newconfuser = models.CharField(max_length=500, default="")
#     newconfpassw = models.CharField(max_length=500, default="")
#     newconfpath = models.CharField(max_length=500, default="")
#     runningIP = models.CharField(max_length=50, default="")
#     testsvn = models.TextField(default="")
#     basesvn = models.TextField(default="")
#     errorlog = models.TextField(default="")
#     cost_test = models.TextField(default="")
#     cost_base = models.TextField(default="")
#     press_qps = models.IntegerField(default=0)
#     press_time = models.IntegerField(default=0)
#     press_expid = models.IntegerField()
#     press_rate = models.FloatField()
#
#     query_ip = models.CharField(max_length=500, default="")
#     query_user = models.CharField(max_length=50, default="")
#     query_pwd = models.CharField(max_length=50, default="")
#     query_path = models.CharField(max_length=500, default="")
#
#     testtag = models.CharField(max_length=500, default="")
# '''
#
# '''
# class DebugQo(models.Model):
#     host_ip = models.CharField(max_length=128)
#     exp_id = models.CharField(max_length=128)
#     query_from = models.CharField(max_length=4, default="")
#     query = models.CharField(max_length=2000)
#     result = models.CharField(max_length=2000)
#     c_time = models.DateTimeField(auto_now=True)
#     # user_fk = models.ForeignKey(to=UserInfo, to_field='username', on_delete=models.CASCADE)
# '''
#
# '''
# class DebugQo(models.Model):
#     host_ip = models.CharField(max_length=128)
#     query_from = models.CharField(max_length=10, default="web")
#     query = models.CharField(max_length=2000)
#     result = models.CharField(max_length=200000)
#     c_time = models.DateTimeField(auto_now=True)
#     # user_fk = models.ForeignKey(to=UserInfo, to_field='username', on_delete=models.CASCADE)
# '''

# status: 0 任务创建 1 任务运行中 2 任务已完成
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    start_time = models.CharField(max_length=50, default="")
    end_time = models.CharField(max_length=50, default="")
    status = models.IntegerField(default=0)



# status: 0 未解决 1 已解决 2 无问题
class ResultDetail(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    query_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=500, default="")
    query_from = models.CharField(max_length=50, default="")
    sg_res_type = models.CharField(max_length=50, default="")
    bd_res_type = models.CharField(max_length=50, default="")
    sg_scene = models.CharField(max_length=500, default="")
    bd_scene = models.CharField(max_length=500, default="")
    status = models.IntegerField(default=0)







