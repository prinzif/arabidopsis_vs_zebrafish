from pymol import cmd

cmd.load("C:/Users/viola/Desktop/datasets/biopython/3d/AF-F1R166-F1-model_v4.pdb", "zebrafish")
cmd.load("C:/Users/viola/Desktop/datasets/biopython/3d/AF-F4HV96-F1-model_v4.pdb", "arabidopsis")

align_result = cmd.align("zebrafish", "arabidopsis")

rmsd_value = align_result[0]  

print("Number of atoms aligned:", align_result[1])
