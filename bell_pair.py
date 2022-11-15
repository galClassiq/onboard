from classiq import ModelDesigner, QUInt
from classiq.builtin_functions.standard_gates import CXGate, HGate
from classiq.interface.generator.model import Constraints

constraints = Constraints(max_width=3)

model_designer = ModelDesigner(constraints=constraints)
hgate_params = HGate()
cx_params = CXGate()

hgate_out = model_designer.HGate(hgate_params)

cx_tgt = hgate_out["TARGET"]

model_designer.CXGate(cx_params, in_wires={"TARGET": cx_tgt})

circuit = model_designer.synthesize()

circuit.show_interactive()
