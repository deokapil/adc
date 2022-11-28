from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.operation import Operation
from app.models.domain.rwmodel import RWModel


class Entry(IDModelMixin, DateTimeModelMixin, RWModel):
    info: str
    sess_id: str
    retval: str
