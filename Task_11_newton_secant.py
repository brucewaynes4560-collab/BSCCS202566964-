from scipy.optimize import root_scalar

# Find the internal rate of return (IRR) for cash flows
cash_flows = [-1000, 300, 400, 500, 400]

def npv(rate):
    return sum(cash_flows[t] / (1 + rate)**t
               for t in range(len(cash_flows)))

newton = root_scalar(npv, x0=0.1, fprime=None, method="newton")
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant")

print(f"IRR using Newton method: {newton.root:.6%}")
print(f"IRR using Secant method: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.8f}")

# Changed input: add a larger final-year cash flow
cash_flows_changed = [-1000, 300, 400, 500, 600]
def npv_changed(rate):
    return sum(cash_flows_changed[t] / (1 + rate)**t
               for t in range(len(cash_flows_changed)))
changed = root_scalar(npv_changed, x0=0.1, x1=0.2, method="secant")
print(f"IRR after increasing final cash flow: {changed.root:.6%}")
