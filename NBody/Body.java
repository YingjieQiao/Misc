//Author: Yingjie Qiao
//Feb 29, 2020

public class Body {
	// The following are the global variables
	public double xxPos;
	public double yyPos;
	public double xxVel;
	public double yyVel;
	public double mass;
	public String imgFileName;
	private static final double g = 6.67E-11; // This number is a constant and should be never modified
		
	public Body(double xP, double yP, double xV,double yV, double m, String img) {
		// To instantiate a body
		xxPos = xP;
		yyPos = yP;
		xxVel = xV;
		yyVel = yV;
		mass = m;
		imgFileName = img;
		// The global variables defined earlier are given values here
	}
	
	public Body(Body b) {
		// To instantiate an identical body
		xxPos = b.xxPos;
		yyPos = b.yyPos;
		xxVel = b.xxVel;
		yyVel = b.yyVel;
		mass = b.mass;
		imgFileName = b.imgFileName;
	}
	
	public double calcDistance(Body b) {
		double dx = b.xxPos - xxPos;
		double dy = b.yyPos - yyPos;
		return Math.sqrt(dx*dx + dy*dy);
	}
	
	public double calcForceExertedBy(Body b) {
		double r = calcDistance(b);
		return  g*mass*b.mass/(r*r);
	}
	
	public double calcForceExertedByX(Body b) {
		double netForce = calcForceExertedBy(b);
		double dx = b.xxPos - xxPos;
		double r = calcDistance(b);
		return netForce*(dx/r);
	}
	
	public double calcForceExertedByY(Body b) {
		double netForce = calcForceExertedBy(b);
		double dy = b.yyPos - yyPos;
		double r = calcDistance(b);
		return netForce*(dy/r);
	}
	
	public double calcNetForceExertedByX(Body[] bodies) {
		double netForce_x = 0;
		//instead of for (i = 0; i < ar.length; i++) 
		for (Body b: bodies) {
			if (!this.equals(b)) {
				netForce_x += calcForceExertedByX(b);
			}
		}
		return netForce_x;
	}
	
	public double calcNetForceExertedByY(Body[] bodies) {
			double netForce_y = 0;
			//instead of for (i = 0; i < ar.length; i++) 
			for (Body b: bodies) {
				if (!this.equals(b)) {
					netForce_y += calcForceExertedByY(b);
				}
			}
			return netForce_y;
	}
	
	public void update(double fxx, double fyy, double dt) {
		double axx = fxx/mass;
		double ayy = fyy/mass;
		xxVel += axx*dt;
		yyVel += ayy*dt;
		xxPos += xxVel*dt;
		yyPos += yyVel*dt;
		
	}
	
	public void draw() {
		StdDraw.picture(xxPos, yyPos, "images/" + imgFileName);
	}
	

}