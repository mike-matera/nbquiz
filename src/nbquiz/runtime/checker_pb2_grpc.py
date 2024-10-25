# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from nbquiz.runtime import checker_pb2 as nbquiz_dot_runtime_dot_checker__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in nbquiz/runtime/checker_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CheckerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.run_tests = channel.unary_unary(
                '/checker.Checker/run_tests',
                request_serializer=nbquiz_dot_runtime_dot_checker__pb2.TestRequest.SerializeToString,
                response_deserializer=nbquiz_dot_runtime_dot_checker__pb2.TestReply.FromString,
                _registered_method=True)


class CheckerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def run_tests(self, request, context):
        """Tests student code while keeping source opaque.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CheckerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'run_tests': grpc.unary_unary_rpc_method_handler(
                    servicer.run_tests,
                    request_deserializer=nbquiz_dot_runtime_dot_checker__pb2.TestRequest.FromString,
                    response_serializer=nbquiz_dot_runtime_dot_checker__pb2.TestReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'checker.Checker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('checker.Checker', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Checker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def run_tests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/checker.Checker/run_tests',
            nbquiz_dot_runtime_dot_checker__pb2.TestRequest.SerializeToString,
            nbquiz_dot_runtime_dot_checker__pb2.TestReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)