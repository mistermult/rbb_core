# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.bag_summary import BagSummary  # noqa: F401,E501
from rbb_swagger_server.models.product import Product  # noqa: F401,E501
from rbb_swagger_server.models.tag import Tag  # noqa: F401,E501
from rbb_swagger_server.models.topic import Topic  # noqa: F401,E501
from rbb_swagger_server import util


class BagDetailed(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, detail_type: str=None, name: str=None, store_data: object=None, discovered: datetime=None, extraction_failure: bool=None, in_trash: bool=None, is_extracted: bool=None, meta_available: bool=None, size: int=None, start_time: datetime=None, end_time: datetime=None, duration: float=None, messages: int=None, tags: List[Tag]=None, topics: List[Topic]=None, products: List[Product]=None, comment: str=None):  # noqa: E501
        """BagDetailed - a model defined in Swagger

        :param detail_type: The detail_type of this BagDetailed.  # noqa: E501
        :type detail_type: str
        :param name: The name of this BagDetailed.  # noqa: E501
        :type name: str
        :param store_data: The store_data of this BagDetailed.  # noqa: E501
        :type store_data: object
        :param discovered: The discovered of this BagDetailed.  # noqa: E501
        :type discovered: datetime
        :param extraction_failure: The extraction_failure of this BagDetailed.  # noqa: E501
        :type extraction_failure: bool
        :param in_trash: The in_trash of this BagDetailed.  # noqa: E501
        :type in_trash: bool
        :param is_extracted: The is_extracted of this BagDetailed.  # noqa: E501
        :type is_extracted: bool
        :param meta_available: The meta_available of this BagDetailed.  # noqa: E501
        :type meta_available: bool
        :param size: The size of this BagDetailed.  # noqa: E501
        :type size: int
        :param start_time: The start_time of this BagDetailed.  # noqa: E501
        :type start_time: datetime
        :param end_time: The end_time of this BagDetailed.  # noqa: E501
        :type end_time: datetime
        :param duration: The duration of this BagDetailed.  # noqa: E501
        :type duration: float
        :param messages: The messages of this BagDetailed.  # noqa: E501
        :type messages: int
        :param tags: The tags of this BagDetailed.  # noqa: E501
        :type tags: List[Tag]
        :param topics: The topics of this BagDetailed.  # noqa: E501
        :type topics: List[Topic]
        :param products: The products of this BagDetailed.  # noqa: E501
        :type products: List[Product]
        :param comment: The comment of this BagDetailed.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'detail_type': str,
            'name': str,
            'store_data': object,
            'discovered': datetime,
            'extraction_failure': bool,
            'in_trash': bool,
            'is_extracted': bool,
            'meta_available': bool,
            'size': int,
            'start_time': datetime,
            'end_time': datetime,
            'duration': float,
            'messages': int,
            'tags': List[Tag],
            'topics': List[Topic],
            'products': List[Product],
            'comment': str
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'name': 'name',
            'store_data': 'store_data',
            'discovered': 'discovered',
            'extraction_failure': 'extraction_failure',
            'in_trash': 'in_trash',
            'is_extracted': 'is_extracted',
            'meta_available': 'meta_available',
            'size': 'size',
            'start_time': 'start_time',
            'end_time': 'end_time',
            'duration': 'duration',
            'messages': 'messages',
            'tags': 'tags',
            'topics': 'topics',
            'products': 'products',
            'comment': 'comment'
        }

        self._detail_type = detail_type
        self._name = name
        self._store_data = store_data
        self._discovered = discovered
        self._extraction_failure = extraction_failure
        self._in_trash = in_trash
        self._is_extracted = is_extracted
        self._meta_available = meta_available
        self._size = size
        self._start_time = start_time
        self._end_time = end_time
        self._duration = duration
        self._messages = messages
        self._tags = tags
        self._topics = topics
        self._products = products
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'BagDetailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BagDetailed of this BagDetailed.  # noqa: E501
        :rtype: BagDetailed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail_type(self) -> str:
        """Gets the detail_type of this BagDetailed.


        :return: The detail_type of this BagDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type: str):
        """Sets the detail_type of this BagDetailed.


        :param detail_type: The detail_type of this BagDetailed.
        :type detail_type: str
        """
        if detail_type is None:
            raise ValueError("Invalid value for `detail_type`, must not be `None`")  # noqa: E501

        self._detail_type = detail_type

    @property
    def name(self) -> str:
        """Gets the name of this BagDetailed.


        :return: The name of this BagDetailed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BagDetailed.


        :param name: The name of this BagDetailed.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def store_data(self) -> object:
        """Gets the store_data of this BagDetailed.

        Data that is specific to the bag store type.  # noqa: E501

        :return: The store_data of this BagDetailed.
        :rtype: object
        """
        return self._store_data

    @store_data.setter
    def store_data(self, store_data: object):
        """Sets the store_data of this BagDetailed.

        Data that is specific to the bag store type.  # noqa: E501

        :param store_data: The store_data of this BagDetailed.
        :type store_data: object
        """
        if store_data is None:
            raise ValueError("Invalid value for `store_data`, must not be `None`")  # noqa: E501

        self._store_data = store_data

    @property
    def discovered(self) -> datetime:
        """Gets the discovered of this BagDetailed.

        Date and time this bag was discovered.  # noqa: E501

        :return: The discovered of this BagDetailed.
        :rtype: datetime
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered: datetime):
        """Sets the discovered of this BagDetailed.

        Date and time this bag was discovered.  # noqa: E501

        :param discovered: The discovered of this BagDetailed.
        :type discovered: datetime
        """
        if discovered is None:
            raise ValueError("Invalid value for `discovered`, must not be `None`")  # noqa: E501

        self._discovered = discovered

    @property
    def extraction_failure(self) -> bool:
        """Gets the extraction_failure of this BagDetailed.

        True if the extraction failed  # noqa: E501

        :return: The extraction_failure of this BagDetailed.
        :rtype: bool
        """
        return self._extraction_failure

    @extraction_failure.setter
    def extraction_failure(self, extraction_failure: bool):
        """Sets the extraction_failure of this BagDetailed.

        True if the extraction failed  # noqa: E501

        :param extraction_failure: The extraction_failure of this BagDetailed.
        :type extraction_failure: bool
        """

        self._extraction_failure = extraction_failure

    @property
    def in_trash(self) -> bool:
        """Gets the in_trash of this BagDetailed.

        True if the bag is in the trash bin.  # noqa: E501

        :return: The in_trash of this BagDetailed.
        :rtype: bool
        """
        return self._in_trash

    @in_trash.setter
    def in_trash(self, in_trash: bool):
        """Sets the in_trash of this BagDetailed.

        True if the bag is in the trash bin.  # noqa: E501

        :param in_trash: The in_trash of this BagDetailed.
        :type in_trash: bool
        """

        self._in_trash = in_trash

    @property
    def is_extracted(self) -> bool:
        """Gets the is_extracted of this BagDetailed.

        True if data is extracted from this bag.  # noqa: E501

        :return: The is_extracted of this BagDetailed.
        :rtype: bool
        """
        return self._is_extracted

    @is_extracted.setter
    def is_extracted(self, is_extracted: bool):
        """Sets the is_extracted of this BagDetailed.

        True if data is extracted from this bag.  # noqa: E501

        :param is_extracted: The is_extracted of this BagDetailed.
        :type is_extracted: bool
        """
        if is_extracted is None:
            raise ValueError("Invalid value for `is_extracted`, must not be `None`")  # noqa: E501

        self._is_extracted = is_extracted

    @property
    def meta_available(self) -> bool:
        """Gets the meta_available of this BagDetailed.

        True if meta data is known for this bag.  # noqa: E501

        :return: The meta_available of this BagDetailed.
        :rtype: bool
        """
        return self._meta_available

    @meta_available.setter
    def meta_available(self, meta_available: bool):
        """Sets the meta_available of this BagDetailed.

        True if meta data is known for this bag.  # noqa: E501

        :param meta_available: The meta_available of this BagDetailed.
        :type meta_available: bool
        """
        if meta_available is None:
            raise ValueError("Invalid value for `meta_available`, must not be `None`")  # noqa: E501

        self._meta_available = meta_available

    @property
    def size(self) -> int:
        """Gets the size of this BagDetailed.

        Size of the bag in bytes.  # noqa: E501

        :return: The size of this BagDetailed.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this BagDetailed.

        Size of the bag in bytes.  # noqa: E501

        :param size: The size of this BagDetailed.
        :type size: int
        """

        self._size = size

    @property
    def start_time(self) -> datetime:
        """Gets the start_time of this BagDetailed.

        Start time of this bag.  # noqa: E501

        :return: The start_time of this BagDetailed.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        """Sets the start_time of this BagDetailed.

        Start time of this bag.  # noqa: E501

        :param start_time: The start_time of this BagDetailed.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self) -> datetime:
        """Gets the end_time of this BagDetailed.

        Start time of this bag.  # noqa: E501

        :return: The end_time of this BagDetailed.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        """Sets the end_time of this BagDetailed.

        Start time of this bag.  # noqa: E501

        :param end_time: The end_time of this BagDetailed.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def duration(self) -> float:
        """Gets the duration of this BagDetailed.

        duration of this bag in seconds.  # noqa: E501

        :return: The duration of this BagDetailed.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        """Sets the duration of this BagDetailed.

        duration of this bag in seconds.  # noqa: E501

        :param duration: The duration of this BagDetailed.
        :type duration: float
        """

        self._duration = duration

    @property
    def messages(self) -> int:
        """Gets the messages of this BagDetailed.

        Number of messages in this bag.  # noqa: E501

        :return: The messages of this BagDetailed.
        :rtype: int
        """
        return self._messages

    @messages.setter
    def messages(self, messages: int):
        """Sets the messages of this BagDetailed.

        Number of messages in this bag.  # noqa: E501

        :param messages: The messages of this BagDetailed.
        :type messages: int
        """

        self._messages = messages

    @property
    def tags(self) -> List[Tag]:
        """Gets the tags of this BagDetailed.


        :return: The tags of this BagDetailed.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[Tag]):
        """Sets the tags of this BagDetailed.


        :param tags: The tags of this BagDetailed.
        :type tags: List[Tag]
        """

        self._tags = tags

    @property
    def topics(self) -> List[Topic]:
        """Gets the topics of this BagDetailed.


        :return: The topics of this BagDetailed.
        :rtype: List[Topic]
        """
        return self._topics

    @topics.setter
    def topics(self, topics: List[Topic]):
        """Sets the topics of this BagDetailed.


        :param topics: The topics of this BagDetailed.
        :type topics: List[Topic]
        """
        if topics is None:
            raise ValueError("Invalid value for `topics`, must not be `None`")  # noqa: E501

        self._topics = topics

    @property
    def products(self) -> List[Product]:
        """Gets the products of this BagDetailed.


        :return: The products of this BagDetailed.
        :rtype: List[Product]
        """
        return self._products

    @products.setter
    def products(self, products: List[Product]):
        """Sets the products of this BagDetailed.


        :param products: The products of this BagDetailed.
        :type products: List[Product]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def comment(self) -> str:
        """Gets the comment of this BagDetailed.

        Manual comment on the bag.  # noqa: E501

        :return: The comment of this BagDetailed.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this BagDetailed.

        Manual comment on the bag.  # noqa: E501

        :param comment: The comment of this BagDetailed.
        :type comment: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment