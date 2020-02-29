//Author: Yingjie Qiao
//Feb 29, 2020

public class NBody {
	public static double readRadius(String filename) {
		In in = new In(filename);
		int N = in.readInt(); // To get by the first integer (number of planets)
		double R = in.readDouble(); //Radius of universe
		return R;
	}
	
	public static Body[] readBodies(String filename) {
		In in = new In(filename);
		int N = in.readInt(); // To get by the first integer (number of planets)
		double R = in.readDouble(); // To get by the first decimal number, radiuds of universe (which is not relevant to this method)
		
		Body[] bodies = new Body[N];
		for (int i = 0; i < N; i++) {
			double xxPos = in.readDouble();
			double yyPos = in.readDouble();
			double xxVel = in.readDouble();
			double yyVel = in.readDouble();
			double mass = in.readDouble();
			String imgFileName = in.readString();
			
			bodies[i] = new Body(xxPos, yyPos, xxVel, yyVel, mass, imgFileName);
		}
		return bodies;
	}
	
	public static void main(String[] args) {
		double T = Double.parseDouble(args[0]);
		double dt = Double.parseDouble(args[1]);
		String filename = args[2];
		
		double radius = readRadius(filename);
		Body[] bodies = readBodies(filename);
		int N = bodies.length;
		
		StdDraw.setScale(-radius, radius);
		StdDraw.clear();
		StdDraw.picture(0, 0, "images/starfield.jpg");
		/*
		for (Body b: bodies) {
			b.draw();
		}
		*/
		StdDraw.enableDoubleBuffering(); //prevent flickering
		double time = 0;
		while (time < T) {
			double[] forces_x = new double[N];
			double[] forces_y = new double[N];
			for (int i = 0; i < N; i++) {
				forces_x[i] = bodies[i].calcNetForceExertedByX(bodies);
				forces_y[i] = bodies[i].calcNetForceExertedByY(bodies);
				//bodies[i].update(dt, forces_x[i], forces_y[i]); // To make autograder happy, comment this line and uncomment the loop below
			}
			
			
			for (int i = 0; i < N; i++) {
				bodies[i].update(forces_x[i], forces_y[i], dt);
				// To make autograder happy
			}
			
			StdDraw.picture(0, 0, "images/starfield.jpg");
			for (Body b: bodies) {
				b.draw();
			}
			StdDraw.show();
			StdDraw.pause(10);
			time += dt;
		}
		StdOut.printf("%d\n", bodies.length);
		StdOut.printf("%.2e\n", radius);
		for (int i = 0; i < bodies.length; i++) {
			StdOut.printf("%11.4e %11.4e %11.4e %11.4e %11.4e %12s\n",
						bodies[i].xxPos, bodies[i].yyPos, bodies[i].xxVel,
						bodies[i].yyVel, bodies[i].mass, bodies[i].imgFileName); 
		}
			
}
}