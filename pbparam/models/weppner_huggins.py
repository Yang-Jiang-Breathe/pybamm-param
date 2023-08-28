#
# Weppner Huggins Model
#
import pybamm
import numpy as np


class WeppnerHuggins(pybamm.lithium_ion.BaseModel):
    """WeppnerHuggins Model for GITT.

    Parameters
    ----------
    name : str, optional
        The name of the model.
    """

    def __init__(self, name="WeppnerHuggins model"):
        super().__init__({}, name)
        # `param` is a class containing all the relevant parameters and functions for
        # this model. These are purely symbolic at this stage, and will be set by the
        # `ParameterValues` class when the model is processed.
        param = self.param
        t = pybamm.t
        ######################
        # Parameters
        ######################
        d_s = param.p.prim.D
        # d_s = pybamm.Parameter("Positive electrode diffusivity [m2.s-1]")

        i_app = param.current_density_with_time

        U = pybamm.Parameter("Reference OCP [V]")

        Uprime = pybamm.Parameter("Derivative of the OCP wrt stoichiometry [V]")

        epsilon = pybamm.Parameter(
            "Positive electrode active material volume fraction"
        )  # param.p.prim.epsilon_s#

        r_particle = pybamm.Parameter("Positive particle radius [m]")  # param.p.prim.R#

        a = 3 * (epsilon / r_particle)

        F = param.F  # pybamm.Parameter("Faraday constant [C.mol-1]")

        l_w = param.p.L  # pybamm.Parameter("Positive electrode thickness [m]")

        ######################
        # Governing equations
        ######################
        u_surf = (
            (2 / np.pi) * (i_app / (pybamm.sqrt(d_s) * a * F * l_w)) * pybamm.sqrt(t)
        )
        # Linearised voltage
        V = U + Uprime * u_surf
        ######################
        # (Some) variables
        ######################
        self.variables = {
            # "Positive particle surface concentration [mol.m-3]":
            # pybamm.PrimaryBroadcast(u_surf,"positive electrode"
            # ),
            "Voltage [V]": V,
        }

    @property
    def default_geometry(self):
        return {}

    @property
    def default_submesh_types(self):
        return {}

    @property
    def default_var_pts(self):
        return {}

    @property
    def default_spatial_methods(self):
        return {}

    @property
    def default_solver(self):
        return pybamm.DummySolver()
