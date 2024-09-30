from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact(_Jac.Walker):

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, world!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body(_Jac.Walker):
    name: str

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class add_two_str(_Jac.Walker):
    s1: str
    s2: str

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': self.s1 + ' ' + self.s2})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', None)], on_exit=[])
@__jac_dataclass__(eq=False)
class simple_interest(_Jac.Walker):
    principal: float
    rate: float
    time: float

    def return_message(self, _jac_here_) -> None:
        _Jac.report({'response': 'Simple Interest: ' + str(self.principal * self.rate * self.time / 100) + ' USD'})