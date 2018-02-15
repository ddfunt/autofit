import timeit
import multiprocessing
#freq, dipoles, constants, constraints, J_min="00", inten="-10.0"):
test_case = """\
constants = {'A': 3000, 'B':2000, 'C': 1000, 'delta_J':2E-4, 'delta_JK':2E-4, 'delta_K':2E-4, 'd_J':2E-4, 'd_K':2E-4, 'spin':0}
dipoles = {'mu_A': 1, 'mu_B': 1, 'mu_C': 1}
constraints = {'maxJ': 20, 'temp': 2,}
int_writer(dipoles=dipoles, constants=constants, constraints=constraints,
           inten="-10.0", freq="100.0")
var_writer(constants)
run_spcat()
"""
def time_estimate():

    outtime = timeit.timeit(stmt=test_case, number=25, setup="from autofit.IO.spcat import int_writer,var_writer,run_spcat")
    scale_factor_one_proc = outtime / 25.0  # Rought estimated time in seconds for a single triple on one core.
    cores_detected = multiprocessing.cpu_count()
    scale_factor = scale_factor_one_proc / cores_detected  # Rough estimated time in seconds for a single triple, divided by number of processors.

    return scale_factor

if __name__ == '__main__':
    print(time_estimate())