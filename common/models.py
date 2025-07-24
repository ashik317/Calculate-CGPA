from django.db import models
from django.utils.translation import gettext_lazy as _

class GradeChoice(models.TextChoices):
    A = "A", _("A")
    A_minus = "A-", _("A-")
    B_plus = "B+", _("B+")
    B = "B", _("B")
    B_minus = "B-", _("B-")
    C_plus = "C+", _("C+")
    C = "C", _("C")
    C_minus = "C-", _("C-")
    D_plus = "D+", _("D+")
    D = "D", _("D")
    D_minus = "D-", _("D-")
    F = "F", _("F")