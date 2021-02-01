import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii
import astropy.units as u
import matplotlib.image as mpimg


np.set_printoptions(precision=4, suppress=True, threshold=np.inf)


def problem1():
  diagram = mpimg.imread('cloud_diagram.png')
  plt.figure(figsize=(10, 8))
  plt.imshow(diagram)
  plt.axis('off')


def I_nu(x_space, aR):
  return 1.0 - np.exp(-2.0 * aR * np.cos(np.pi * x_space / 2.0))


def solution1():
  fig, axs = plt.subplots(1, 2, constrained_layout=True)
  fig.suptitle('Specific intensity profiles when viewing face of star')

  I_label = r'Specific intensity ($\frac{I_\nu}{S_\nu}$)'
  b_label = r'Impact parameter ($\frac{b}{R}$)'
  lims = [-1.0, 1.0]
  x_space = np.linspace(lims[0], lims[1], 100)

  aR = 0.01
  axs[0].set_title(r'$\alpha_\nu R$ = ' f'{aR:.2f}')
  axs[0].plot(x_space, I_nu(x_space, aR))
  axs[0].set_xlabel(b_label)
  axs[0].set_ylabel(I_label)
  aR = 3.0
  axs[1].set_title(r'$\alpha_\nu R$ = ' f'{aR:.2f}')
  axs[1].plot(x_space, I_nu(x_space, aR))
  axs[1].set_xlabel(b_label)
  axs[1].set_ylabel(I_label)
  plt.savefig('hw1_1.png')


def solution2():
  data = ascii.read('comacluster_mushotzky.csv', format='csv')
  assert 'ekev' in data.keys()
  assert 'nekev' in data.keys()

  with u.set_enabled_equivalencies(u.spectral()):
    data['ekev'].unit = u.keV
    data['ehz'] = data['ekev'].to(u.Hz)
    data['nekev'].unit = u.cm ** -2 / u.s / u.keV
    data['Fhz'] = data['ekev'].to(u.erg) * data['nekev'] * (1.0 * u.keV) / (1.0 * u.keV).to(u.Hz)
    D = (100.0 * u.Mpc).to(u.cm)
    R = (1.0 * u.Mpc).to(u.cm)
    data['vLhz'] = 4 * np.pi * D ** 2 * data['Fhz'] * data['ehz']

  ascii.write(data, 'hw1_2.csv', format='csv', overwrite=True)
  plt.plot(np.log10(data['ehz']), np.log10(data['vLhz']))
  plt.suptitle('Flux density spectrum of Coma Cluster')
  plt.xlabel(r'Frequency $\log(\nu)$ [Hz]')
  plt.ylabel(r'Flux density $\log(\nu L_\nu)$ [erg/s]')
  plt.savefig('hw1_2.png')


if __name__ == '__main__':
  solution1()
