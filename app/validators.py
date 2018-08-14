from django.core.validators import BaseValidator
from django.utils.translation import ugettext as _


class FileSizeValidator(BaseValidator):
    """
    Validate file size. Size must be given in Kb.
    """
    message = _('El archivo debe ser máximo de 4MB')
    code = 'file_size'

    def compare(self, a, b):
        return a.size > 1024 * b
