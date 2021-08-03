/*
 * This Software is under the MIT License
 * Refer to LICENSE or https://opensource.org/licenses/MIT for more information
 * Copyright (c) 2019, Kohulan Rajan
 */

import java.text.DecimalFormat;

import java.io.*;

import org.openscience.cdk.DefaultChemObjectBuilder;
import org.openscience.cdk.inchi.InChIGeneratorFactory;
import org.openscience.cdk.inchi.InChIToStructure;
import org.openscience.cdk.interfaces.IAtomContainer;
import org.openscience.cdk.io.SDFWriter;
import org.openscience.cdk.layout.StructureDiagramGenerator;
import org.openscience.cdk.smiles.SmiFlavor;
import org.openscience.cdk.smiles.SmilesGenerator;
import org.openscience.cdk.smiles.SmilesParser;


public class InchitoSMILES {
	String temp = "";
	String moleculeTitle = null;
	int moleculeCount = 0;
	boolean verbose = false;

	public static void main(String[] args) throws Exception {
		long startTime = System.nanoTime();
		for (String s : args) {
		SmilesGenerator sg = new SmilesGenerator(SmiFlavor.Absolute);
		

		// Directories according to your data files
		String file_name = s.substring(0, s.length());
		File fileout = new File(file_name + "_SMILES.txt");
		if (!fileout.exists()) {
			fileout.createNewFile();
		}
		FileWriter bufferWriter = new FileWriter(fileout.getAbsoluteFile(), true);
		BufferedReader input_file = new BufferedReader(new FileReader(s));
		String line = input_file.readLine();
		while (line != null) {
			String[] splitted_line = line.split("\t");
			try {
			SmilesParser smi = new SmilesParser(DefaultChemObjectBuilder.getInstance());
			IAtomContainer molecule1 = InChIGeneratorFactory.getInstance().getInChIToStructure((splitted_line[0]), DefaultChemObjectBuilder.getInstance()).getAtomContainer();
			//IAtomContainer molecule1 = smi.parseSmiles(splitted_line[0]);
			
			StructureDiagramGenerator sdg = new StructureDiagramGenerator();
			sdg.setMolecule(molecule1);
			sdg.generateCoordinates(molecule1);
			molecule1 = sdg.getMolecule();
			String smi_ori = sg.create(molecule1);
			
			bufferWriter.write(smi_ori+"\t"+splitted_line[1] + "\n");
			//System.out.println(smi_ori+"\t"+splitted_line[1] + "\n");
		}
			 catch(Exception e) { 
			 	//System.out.println(splitted_line[1]+"\tRejected\n");
			 	bufferWriter.write(splitted_line[1]+"\tRejected\n");
			 }
			

			line = input_file.readLine();
		}
		bufferWriter.flush();
		bufferWriter.close();
		input_file.close();
		long endTime = System.nanoTime() - startTime;
		double seconds = (double) endTime / 1000000000.0;
		DecimalFormat d = new DecimalFormat(".###");
		System.out.println(
				"SDFs arrays generated..\nAll images rendered successfully!! Time: " + d.format(seconds) + " seconds");
	}}
}
