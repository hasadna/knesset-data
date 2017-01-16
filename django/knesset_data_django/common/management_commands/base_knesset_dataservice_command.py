from knesset_data_django.common.management_commands.base_no_args_command import BaseNoArgsCommand


class BaseKnessetDataserviceCommand(BaseNoArgsCommand):
    """
    A base command to ease fetching the data from the knesset API into the app schema

    extending classes should implement the functions that raise NotImplementError exceptions
    """

    _DS_TO_APP_KEY_MAPPING = tuple()
    _DS_CONVERSIONS = {}

    def _has_existing_object(self, dataservice_object):
        return self._get_existing_object(dataservice_object) is not None

    def _get_existing_object(self, dataservice_object):
        # should use the dataservice_object to get existing related object in DB
        # if related object is not in DB - should return None
        # example code:
        # qs = Vote.objects.filter(src_id=dataservice_object.id)
        # return qs.first() if qs.count() == 1 else None
        raise NotImplementedError()

    def _create_new_object(self, dataservice_object):
        """
        this will run after get_existing_object, so you can assume there is no existing object in DB
        it should create the object in DB using the data in dataservice_object
        return value is the created DB object
        this function must always return a DB object which was created - if there is an error - raise an Exception
        Args:
            dataservice_object:

        Returns:

        """
        raise NotImplementedError()

    def recreate_objects(self, object_ids):
        # recreate the given list of DB object ids
        # this could be something that deletes, then re-creates
        # or it could update in-place
        # example code which just deletes and re-creates (usually you will want something more complex):
        # recreated_votes = []
        # for vote_id in vote_ids:
        #     oknesset_vote = Vote.objects.get(id=int(vote_id))
        #     dataservice_vote = self.DATASERVICE_CLASS.get(oknesset_vote.src_id)
        #     oknesset_vote.delete()
        #     recreated_vote = self._create_new_object(dataservice_vote)
        #     recreated_votes.append(self._update_or_create_vote(dataservice_vote, oknesset_vote))
        # return recreated_votes
        raise NotImplementedError()

    def _translate_ds_to_model(self, ds_meeting):
        """
        The function provide a mapping service from knesset-data data structure to the app schema using
        the `translate_ds_to_model` . In order to use, fill the `_DS_TO_APP_KEY_MAPPING` and
        `_DS_CONVERSIONS` in the inheriting class in the following manner:

            _DS_TO_APP_KEY_MAPPING = ((app_key, knesset_data_key),(app_key, knesset_data_key)...)
            _DS_CONVERSIONS = {app_key: conversion_fn, ...}

        This will take the attributes from the knesset-data class and will yield a key, value tuples
        with the new key and the value conversion (if any).

        :param ds_meeting: The knesset data service class
        """
        for model_key, ds_key in self._DS_TO_APP_KEY_MAPPING:
            val = getattr(ds_meeting, ds_key)
            if model_key in self._DS_CONVERSIONS:
                val = self._DS_CONVERSIONS[model_key](val)
            yield model_key, val

    def handle_noargs(self, **options):
        super(BaseKnessetDataserviceCommand, self).handle_noargs(**options)
