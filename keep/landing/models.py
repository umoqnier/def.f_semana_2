from django.db import models


class Remainder(models.Model):
	PRIORIDADES = (
			("AT","Alta"),
			("NR","Normal"),
			("BJ","Baja"),
		)
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()
	prioridad = models.CharField(max_length=30, choices=PRIORIDADES)
	fecha_creacion = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Remainder N° %s sobre: %s" % (str(self.id), str(self.titulo))

