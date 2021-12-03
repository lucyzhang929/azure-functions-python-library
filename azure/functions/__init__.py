# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from ._abc import TimerRequest, InputStream, Context, Out
from ._eventhub import EventHubEvent
from ._eventgrid import EventGridEvent, EventGridOutputEvent
from ._cosmosdb import Document, DocumentList
from ._http import HttpRequest
from ._http import HttpResponse
from ._http_wsgi import WsgiMiddleware
from ._http_asgi import AsgiMiddleware
from .kafka import KafkaEvent, KafkaConverter, KafkaTriggerConverter
from ._queue import QueueMessage
from ._servicebus import ServiceBusMessage
from ._durable_functions import OrchestrationContext, EntityContext
from .meta import get_binding_registry
from .extension import (ExtensionMeta, FunctionExtensionException,
                        FuncExtensionBase, AppExtensionBase)
from ._decorators import DataType
from .decorators import AuthLevel, BlobInput, BlobOutput, EventHubTrigger, \
    FunctionsApp, Http, HttpMethod, HttpTrigger

# Import binding implementations to register them
from . import blob  # NoQA
from . import cosmosdb  # NoQA
from . import eventgrid  # NoQA
from . import eventhub  # NoQA
from . import http  # NoQA
from . import kafka # NoQA
from . import queue  # NoQA
from . import servicebus  # NoQA
from . import timer  # NoQA
from . import durable_functions  # NoQA


__all__ = (
    # Functions
    'get_binding_registry',

    # Generics.
    'Context',
    'Out',

    # Binding rich types, sorted alphabetically.
    'Document',
    'DocumentList',
    'EventGridEvent',
    'EventGridOutputEvent',
    'EventHubEvent',
    'HttpRequest',
    'HttpResponse',
    'InputStream',
    'KafkaEvent',
    'KafkaConverter',
    'KafkaTriggerConverter',
    'OrchestrationContext',
    'EntityContext',
    'QueueMessage',
    'ServiceBusMessage',
    'TimerRequest',

    # Middlewares
    'WsgiMiddleware',
    'AsgiMiddleware',

    # Extensions
    'AppExtensionBase',
    'FuncExtensionBase',
    'ExtensionMeta',
    'FunctionExtensionException',

    ### Decorators
    # 'BlobInput',
    # 'BlobOutput',
    # 'DataType',
    # 'EventHubTrigger',
    'FunctionsApp',
    # 'HttpTrigger',
    # 'HttpMethod',
    # 'Http'
)

__version__ = '1.8.0'
