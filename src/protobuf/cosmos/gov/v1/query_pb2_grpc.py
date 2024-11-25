"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.gov.v1 import query_pb2 as cosmos_dot_gov_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service for gov module
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Constitution = channel.unary_unary('/cosmos.gov.v1.Query/Constitution', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionResponse.FromString)
        self.Proposal = channel.unary_unary('/cosmos.gov.v1.Query/Proposal', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalResponse.FromString)
        self.Proposals = channel.unary_unary('/cosmos.gov.v1.Query/Proposals', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsResponse.FromString)
        self.Vote = channel.unary_unary('/cosmos.gov.v1.Query/Vote', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteResponse.FromString)
        self.Votes = channel.unary_unary('/cosmos.gov.v1.Query/Votes', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesResponse.FromString)
        self.Params = channel.unary_unary('/cosmos.gov.v1.Query/Params', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.Deposit = channel.unary_unary('/cosmos.gov.v1.Query/Deposit', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositResponse.FromString)
        self.Deposits = channel.unary_unary('/cosmos.gov.v1.Query/Deposits', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsResponse.FromString)
        self.TallyResult = channel.unary_unary('/cosmos.gov.v1.Query/TallyResult', request_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultRequest.SerializeToString, response_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service for gov module
    """

    def Constitution(self, request, context):
        """Constitution queries the chain's constitution.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Proposal(self, request, context):
        """Proposal queries proposal details based on ProposalID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Proposals(self, request, context):
        """Proposals queries all proposals based on given status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Vote(self, request, context):
        """Vote queries voted information based on proposalID, voterAddr.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Votes(self, request, context):
        """Votes queries votes of a given proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters of the gov module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Deposit queries single deposit information based on proposalID, depositAddr.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposits(self, request, context):
        """Deposits queries all deposits of a single proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TallyResult(self, request, context):
        """TallyResult queries the tally of a proposal vote.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Constitution': grpc.unary_unary_rpc_method_handler(servicer.Constitution, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionResponse.SerializeToString), 'Proposal': grpc.unary_unary_rpc_method_handler(servicer.Proposal, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalResponse.SerializeToString), 'Proposals': grpc.unary_unary_rpc_method_handler(servicer.Proposals, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsResponse.SerializeToString), 'Vote': grpc.unary_unary_rpc_method_handler(servicer.Vote, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteResponse.SerializeToString), 'Votes': grpc.unary_unary_rpc_method_handler(servicer.Votes, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'Deposit': grpc.unary_unary_rpc_method_handler(servicer.Deposit, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositResponse.SerializeToString), 'Deposits': grpc.unary_unary_rpc_method_handler(servicer.Deposits, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsResponse.SerializeToString), 'TallyResult': grpc.unary_unary_rpc_method_handler(servicer.TallyResult, request_deserializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultRequest.FromString, response_serializer=cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.gov.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service for gov module
    """

    @staticmethod
    def Constitution(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Constitution', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryConstitutionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Proposal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Proposal', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Proposals(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Proposals', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryProposalsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Vote(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Vote', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVoteResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Votes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Votes', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryVotesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Params', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Deposit', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposits(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/Deposits', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryDepositsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TallyResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1.Query/TallyResult', cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultRequest.SerializeToString, cosmos_dot_gov_dot_v1_dot_query__pb2.QueryTallyResultResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)