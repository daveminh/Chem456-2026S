#!/usr/bin/env python
"""
11-SIRS.py

Generate an aligned SIRS trajectory from Exercise 10 Fulton Market output.

Usage
-----
python 11-SIRS.py <MM_system>

Example
-------
python 11-SIRS.py MSX-2
"""

import os
import sys
import numpy as np
import MDAnalysis as mda
from MDAnalysis.coordinates.memory import MemoryReader
from MDAnalysis.analysis import align
from MDAnalysis.transformations.translate import center_in_box
from MDAnalysis import transformations

# ------------------
# Parse command-line arguments
# ------------------
if len(sys.argv) != 2:
    raise RuntimeError(
        "Usage: python 11-SIRS.py <MM_system>\n"
        "Example: python 11-SIRS.py MSX-2"
    )

MM_system = sys.argv[1]

# ------------------
# Paths
# ------------------
base_dir = os.path.expanduser(f'~/exercises/10/{MM_system}')
ref_pdb_fn = os.path.expanduser(f'~/exercises/08/{MM_system}/Step_4.pdb')
out_dir = os.path.expanduser(f'~/exercises/11/{MM_system}')
os.makedirs(out_dir, exist_ok=True)

# ------------------
# Fulton Market analysis
# ------------------
sys.path.append(os.path.expanduser('~/github/FultonMarket'))
from FultonMarket.analysis.FultonMarketAnalysis import FultonMarketAnalysis

fma = FultonMarketAnalysis(base_dir, pdb=ref_pdb_fn)
fma.equilibration_method = 'energy'
fma.resids = None

print(f"[{MM_system}] Performing Sampling Importance Resampling")
fma.importance_resampling()

# Explicitly load saved position data
fma._load_positions_box_vecs()

# ------------------
# Build MDAnalysis universe
# ------------------
u_ref = mda.Universe(ref_pdb_fn)
sel_complex = u_ref.select_atoms('protein or resname UNK')
u = mda.Merge(sel_complex)

print(f"[{MM_system}] Extracting resampled coordinates")

sim_idx = [
    fma.map[iteration, state].astype(int)
    for (state, iteration) in fma.resampled_inds
]

positions = np.array([
    fma.positions[s[0]][s[1], s[2], sel_complex.indices]
    for s in sim_idx
]) * 10.0  # nm → Å

u.load_new(positions, format=MemoryReader)

boxes = np.array([list(np.diag(fma.box_vectors[s[0]][s[1],s[2],:,:]*10)) + [90,90,90] for s in sim_idx])
for (ts, box) in zip(u.trajectory, boxes):
    ts.dimensions = box

# ------------------
# Alignment
# ------------------
print(f"[{MM_system}] Aligning trajectory")

# PBC handling
u.trajectory.add_transformations(
    center_in_box(u.select_atoms('protein')),
    transformations.wrap(u.select_atoms('resname UNK')),
    transformations.unwrap(u.select_atoms('resname UNK'))
)

# Alignment based on transmembrane regions
u_ref2 = mda.Merge(sel_complex)
align.AlignTraj(
    mobile=u,
    reference=u_ref2,
    select='protein and name CA and (resid 8-32 or resid 43-66 or resid 78-100 or resid 121-143 or resid 174-198 or resid 235-258 or resid 267-290)',
    in_memory=True
).run()

# ------------------
# Write outputs
# ------------------
pdb_out = os.path.join(out_dir, f'{MM_system}_SIRS_reference.pdb')
traj_out = os.path.join(out_dir, f'{MM_system}_SIRS_aligned.dcd')

print(f"[{MM_system}] Writing output files")

with mda.Writer(pdb_out) as W:
    W.write(u)

with mda.Writer(traj_out, n_atoms=u.atoms.n_atoms) as W:
    for ts in u.trajectory:
        W.write(u)

print("Done.")
print("Reference PDB:", pdb_out)
print("Trajectory   :", traj_out)