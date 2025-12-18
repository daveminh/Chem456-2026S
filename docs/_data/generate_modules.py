table = """M	8/19	No class - Dr. Minh conference travel	
W	8/21	No class - Dr. Minh conference travel	
M	8/26	Introduction and syllabus. Exercise 1: Introduction to Google Colab.	
W	8/28	Fundamentals of biological macromolecules.  Exercise 2: Structural visualization with py3DMol. During lunch: Structure determination by X-ray crystallography, NMR, and CryoEM	
M	9/2	No class - Labor Day	
W	9/4	Structure prediction principles. Exercise 3: Homology modeling.	Exercise 1. Exercise 2.
M	9/9	Examples of molecular modeling projects.	
W	9/11	Selecting a target for structure-based molecular design. Scientific and market considerations.	Exercise 3.
M	9/16	Surveying the scientific literature. Academic literature databases. Reference management with Zotero.	Quiz: Biomolecular structure.
W	9/18	Biomolecular electrostatics	
M	9/23	Exercise 4: Visualizing protonation and electrostatics	
W	9/25	Biological target presentations	Biological target presentations
M	9/30	Biological target presentations. Decide project teams.	Exercise 4
W	10/2	Molecular docking. Scoring functions. Common optimization algorithms. 	
M	10/7	No class - Fall Break Day	
W	10/9	Exercise 5: Molecular docking with AutoDock Vina	Biological target report
M	10/14	Molecular mechanics force fields. Bonded and nonbonded energy terms. Parameterization.	
W	10/16	Exercise 6: Preparing a system for molecular simulation.	Exercise 5
M	10/21	Quantum mechanics/molecular mechanics (QM/MM)	
W	10/23	Exercise 7: QM/MM analysis of SARS-CoV-2 MPro catalysis	Exercise 6
M	10/28	Monte Carlo. Monte Carlo Integration. Markov chain Monte Carlo.	Quiz: Potential energy
W	10/30	Molecular simulation. Metropolis Monte Carlo. Molecular dynamics. Constrained dynamics. Integrators, thermostats, and barostats. Exercise 8: Performing a molecular simulation with OpenMM	Exercise 7
M	11/4	Exercise 9: Analysis of molecular simulations. Equilibration. Alignment and visualization of trajectories. Root mean square properties. Estimating expectation values. Dimensionality reduction. Clustering.	
W	11/6	Simulating and analyzing thermodynamic processes. Replica exchange.	Exercise 8. ACCESS-CI allocation request.
M	11/11	Exercise 10: Umbrella sampling. Binding free energy calculations. Alchemical methods. Thermodynamic cycles.	Exercise 9
W	11/13	Exercise 11: Replica exchange. Analysis of free energy calculations. Simulation quality metrics.	
M	11/18	Computational Molecular Pharmacology. Signaling through 7 transmembrane receptors.	
W	11/20	Quantitative structure-property relationships. Structural features. Common properties. Machine learning methods.	Exercise 10. Quiz: Molecular simulations
M	11/25	Exercise 12: Machine learning prediction of solvation energies.	Exercise 11.
W	11/27	No class - Thanksgiving Break"""

for row in table.split('\n'):
    cols = row.split('\t')
    day = cols[0]
    date = cols[1]
    record = f"- day: {day}\n  date: {date}\n"
    if len(cols)>2:
        content = cols[2].strip('.')
        basename = content.split('.')[0]
        if content.find("Exercise")>-1:
            exercise_info = content[content.find('Exercise'):].split('.')[0]
            title = content.replace(exercise_info,'')
            if title!="":
                record += f'  title: "{title}"\n'
            record += f'  exercise: "{exercise_info[9:]}"\n'
            if content.find('.')>0:
                basename = content[content.find('.'):]
            else:
                basename = ''
        else:
            title = content
            record += f'  title: "{title}"\n'
        if basename.find('No class')>-1:
            basename = ''
        if basename!="":
            dash_date = '-'.join([f"{int(d):02d}" for d in date.split('/')])
            record += f'  basename_template: "{dash_date}-{basename}"\n'
    if len(cols)>3:
        due = cols[3].strip('.')
        if due!="":
            record += f'  due: "{due}"\n'
    # record += '\n'
    print(record)