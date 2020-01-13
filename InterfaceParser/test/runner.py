"""Main entry point for all unit tests

"""

import sys
from pathlib import Path
from unittest import TestLoader, TestSuite, TextTestRunner

sys.path.append(Path(__file__).absolute().parents[1].as_posix())

try:
    from parsers_test.test_json_rpc import TestJSONRPCVParser
    from parsers_test.test_sdl_rpc_v1 import TestSDLRPCV1Parser
    from parsers_test.test_sdl_rpc_v2 import TestSDLRPCV2Parser
    from test_model import TestInterfaceModel
    from test_code_format_and_quality import CodeFormatAndQuality
except ModuleNotFoundError as error:
    print('{}.\nProbably you did not initialize submodule'.format(error))
    sys.exit(1)

if __name__ == '__main__':
    SUITE = TestSuite()

    SUITE.addTests(TestLoader().loadTestsFromTestCase(TestJSONRPCVParser))
    SUITE.addTests(TestLoader().loadTestsFromTestCase(TestSDLRPCV1Parser))
    SUITE.addTests(TestLoader().loadTestsFromTestCase(TestSDLRPCV2Parser))
    SUITE.addTests(TestLoader().loadTestsFromTestCase(TestInterfaceModel))
    SUITE.addTests(TestLoader().loadTestsFromTestCase(CodeFormatAndQuality))

    RUNNER = TextTestRunner(verbosity=2)
    TEST_RESULT = RUNNER.run(SUITE)
    print(TEST_RESULT)
