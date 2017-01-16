from knesset_data_django.mks.models import Member
from knesset_data_django.persons.models import Person, PersonAlias


def get_all_mk_names():
    mks = []
    mk_names = []
    current_mks = Member.current_knesset.filter(is_current=True)
    mks.extend(current_mks)
    mk_names.extend(current_mks.values_list('name', flat=True))
    current_mk_ids = [m.id for m in current_mks]
    mk_persons = Person.objects.filter(
        mk__isnull=False,
        mk__id__in=current_mk_ids).select_related('mk')
    mk_aliases = PersonAlias.objects.filter(
        person__in=mk_persons).select_related('person', 'person__mk')
    mks.extend([person.mk for person in mk_persons])
    mk_names.extend(mk_persons.values_list('name', flat=True))
    mks.extend([alias.person.mk for alias in mk_aliases])
    mk_names.extend(mk_aliases.values_list('name', flat=True))
    return (mks, mk_names)
