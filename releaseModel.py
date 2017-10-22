

# Vessel -->  (Pipe -->) leak
# Pipeline --> (Pipe -->) leak
# Vessel --> Pipe --> PSV --> Pipe --> Flare
# TODO: install pip for phtyhon3
# TODO: install scipy for python3
# TODO: install thermopy


def IsChokedFlow (p_in, p_atm, gamma):
	''' 
	Function returns True if flow is speed of sound and False if not.
	'''

	pressureRatio = p_in/p_atm
	gammaSide = ((gamma +1)/2)**(gamma/(gamma-1))
	if pressureRatio >= gammaSide:
		return True
	else:
		return False


def LinearVelocity (flowrate, gamma, p_in, p_atm, D_pipe):
	'''
	Function will return the Linear Velocity of the release.
	'''

	pass


def ChokedRelease(c_o, A_h, p, rho_o, gamma):
	'''
	Function returns choked flow rate from orifice from a pressurized source
	c_o = dicharge coefficient for orifice (dimensionless)
	A_h = puncture area (m^2)
	p = pressure
	rho_o = 
	gamma = ratio of specific heats
	'''

	flowrate = c_o*A_h*(p*rho_o*gamma*(2/(gamma+1)**((gamma+1)/(gamma -1))))**(1/2)

	return flowrate


def NonChokedRelease():
	
	pass

