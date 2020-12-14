# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.dialogflow_v2.types import entity_type
from google.cloud.dialogflow_v2.types import entity_type as gcd_entity_type
from google.longrunning import operations_pb2 as operations  # type: ignore
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import EntityTypesTransport, DEFAULT_CLIENT_INFO
from .grpc import EntityTypesGrpcTransport


class EntityTypesGrpcAsyncIOTransport(EntityTypesTransport):
    """gRPC AsyncIO backend transport for EntityTypes.

    Service for managing
    [EntityTypes][google.cloud.dialogflow.v2.EntityType].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "dialogflow.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._ssl_channel_credentials = ssl_channel_credentials

        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )
            self._ssl_channel_credentials = ssl_credentials
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        self._stubs = {}

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def list_entity_types(
        self,
    ) -> Callable[
        [entity_type.ListEntityTypesRequest],
        Awaitable[entity_type.ListEntityTypesResponse],
    ]:
        r"""Return a callable for the list entity types method over gRPC.

        Returns the list of all entity types in the specified
        agent.

        Returns:
            Callable[[~.ListEntityTypesRequest],
                    Awaitable[~.ListEntityTypesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entity_types" not in self._stubs:
            self._stubs["list_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/ListEntityTypes",
                request_serializer=entity_type.ListEntityTypesRequest.serialize,
                response_deserializer=entity_type.ListEntityTypesResponse.deserialize,
            )
        return self._stubs["list_entity_types"]

    @property
    def get_entity_type(
        self,
    ) -> Callable[
        [entity_type.GetEntityTypeRequest], Awaitable[entity_type.EntityType]
    ]:
        r"""Return a callable for the get entity type method over gRPC.

        Retrieves the specified entity type.

        Returns:
            Callable[[~.GetEntityTypeRequest],
                    Awaitable[~.EntityType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entity_type" not in self._stubs:
            self._stubs["get_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/GetEntityType",
                request_serializer=entity_type.GetEntityTypeRequest.serialize,
                response_deserializer=entity_type.EntityType.deserialize,
            )
        return self._stubs["get_entity_type"]

    @property
    def create_entity_type(
        self,
    ) -> Callable[
        [gcd_entity_type.CreateEntityTypeRequest], Awaitable[gcd_entity_type.EntityType]
    ]:
        r"""Return a callable for the create entity type method over gRPC.

        Creates an entity type in the specified agent.

        Returns:
            Callable[[~.CreateEntityTypeRequest],
                    Awaitable[~.EntityType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entity_type" not in self._stubs:
            self._stubs["create_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/CreateEntityType",
                request_serializer=gcd_entity_type.CreateEntityTypeRequest.serialize,
                response_deserializer=gcd_entity_type.EntityType.deserialize,
            )
        return self._stubs["create_entity_type"]

    @property
    def update_entity_type(
        self,
    ) -> Callable[
        [gcd_entity_type.UpdateEntityTypeRequest], Awaitable[gcd_entity_type.EntityType]
    ]:
        r"""Return a callable for the update entity type method over gRPC.

        Updates the specified entity type.

        Returns:
            Callable[[~.UpdateEntityTypeRequest],
                    Awaitable[~.EntityType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entity_type" not in self._stubs:
            self._stubs["update_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/UpdateEntityType",
                request_serializer=gcd_entity_type.UpdateEntityTypeRequest.serialize,
                response_deserializer=gcd_entity_type.EntityType.deserialize,
            )
        return self._stubs["update_entity_type"]

    @property
    def delete_entity_type(
        self,
    ) -> Callable[[entity_type.DeleteEntityTypeRequest], Awaitable[empty.Empty]]:
        r"""Return a callable for the delete entity type method over gRPC.

        Deletes the specified entity type.

        Returns:
            Callable[[~.DeleteEntityTypeRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entity_type" not in self._stubs:
            self._stubs["delete_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/DeleteEntityType",
                request_serializer=entity_type.DeleteEntityTypeRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_entity_type"]

    @property
    def batch_update_entity_types(
        self,
    ) -> Callable[
        [entity_type.BatchUpdateEntityTypesRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch update entity types method over gRPC.

        Updates/Creates multiple entity types in the specified agent.

        Operation <response:
        [BatchUpdateEntityTypesResponse][google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse]>

        Returns:
            Callable[[~.BatchUpdateEntityTypesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_entity_types" not in self._stubs:
            self._stubs["batch_update_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchUpdateEntityTypes",
                request_serializer=entity_type.BatchUpdateEntityTypesRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_update_entity_types"]

    @property
    def batch_delete_entity_types(
        self,
    ) -> Callable[
        [entity_type.BatchDeleteEntityTypesRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch delete entity types method over gRPC.

        Deletes entity types in the specified agent.

        Operation <response:
        [google.protobuf.Empty][google.protobuf.Empty]>

        Returns:
            Callable[[~.BatchDeleteEntityTypesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_entity_types" not in self._stubs:
            self._stubs["batch_delete_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchDeleteEntityTypes",
                request_serializer=entity_type.BatchDeleteEntityTypesRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_delete_entity_types"]

    @property
    def batch_create_entities(
        self,
    ) -> Callable[
        [entity_type.BatchCreateEntitiesRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch create entities method over gRPC.

        Creates multiple new entities in the specified entity type.

        Operation <response:
        [google.protobuf.Empty][google.protobuf.Empty]>

        Returns:
            Callable[[~.BatchCreateEntitiesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_entities" not in self._stubs:
            self._stubs["batch_create_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchCreateEntities",
                request_serializer=entity_type.BatchCreateEntitiesRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_create_entities"]

    @property
    def batch_update_entities(
        self,
    ) -> Callable[
        [entity_type.BatchUpdateEntitiesRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch update entities method over gRPC.

        Updates or creates multiple entities in the specified entity
        type. This method does not affect entities in the entity type
        that aren't explicitly specified in the request.

        Operation <response:
        [google.protobuf.Empty][google.protobuf.Empty]>

        Returns:
            Callable[[~.BatchUpdateEntitiesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_entities" not in self._stubs:
            self._stubs["batch_update_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchUpdateEntities",
                request_serializer=entity_type.BatchUpdateEntitiesRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_update_entities"]

    @property
    def batch_delete_entities(
        self,
    ) -> Callable[
        [entity_type.BatchDeleteEntitiesRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the batch delete entities method over gRPC.

        Deletes entities in the specified entity type.

        Operation <response:
        [google.protobuf.Empty][google.protobuf.Empty]>

        Returns:
            Callable[[~.BatchDeleteEntitiesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_entities" not in self._stubs:
            self._stubs["batch_delete_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchDeleteEntities",
                request_serializer=entity_type.BatchDeleteEntitiesRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["batch_delete_entities"]


__all__ = ("EntityTypesGrpcAsyncIOTransport",)
