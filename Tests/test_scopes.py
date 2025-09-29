import pytest

class TestGroupA:
    def test_one(self, class_resource, module_resource, session_resource):
        print("Running TestGroupA.test_one")

    def test_two(self, class_resource, module_resource, session_resource):
        print("Running TestGroupA.test_two")


class TestGroupB:
    def test_three(self, class_resource, module_resource, session_resource):
        print("Running TestGroupB.test_three")
