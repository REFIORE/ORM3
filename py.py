from datacenter.models import Schoolkid, Mark, Chastisement


schoolkid = Schoolkid.objects.filter(full_name__contains='Фролов Иван').first()
classmate=Schoolkid.objects.filter(full_name__contains='Голубеве Феофане').first()


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
