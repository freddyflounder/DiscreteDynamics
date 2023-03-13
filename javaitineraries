//Andy Vick, 29 Sept 2022, Java Program (Orbit and Itinerary Calculator, discrete dynamics)
//This program is intended for people studying discrete dynamcis. Given an integer k (listed as tuple in program), m_k maps x to kx on R mod Z.
//In dynamics, an orbit is the set of points on R mod Z (which is on [0,1)) that x hits on iterations of m_k until it returns to x.
//The itinerary is obtained by parsing R mod Z into k distinct sectors of equal length and maps from the orbit to a sequence consisting of {1,...,k}
	


import java.util.Scanner;
		public class Inputs{
			//Function to calculate and output the orbit of a point in [0,1) given a multiple
			public static int orbit(int num, int den, int tuple) {
				int i=num, k=0;				//i acts as numerator in loop, k counts iterations of loop
				i*=tuple;					//set i at iteration 1
				k++;						//set k to iteration 1
				
				for(i=i;i!=0;i*=tuple) {	//orbit calculations begin; multiply i by tuple each iteration, i goes to 0 when returns to ic
				i=i%den;					//ensures that orbit never leaves [0,1)/unit circle
				System.out.println("The orbit is now at: "+i+"/"+den);	//reports state of orbit at each iteration
				
				if(i==num)					//condition if i returns to ic
				{
					i=0;					//kick out of loop
				} else {
					k++;					//move onto next iteration otherwise
				}
				};
				System.out.println("The orbit has returned to initial condition in "+k+" iterations.");		//reports k upon return to ic
				return k;			//k value returned to be used in itinerary function
			}
			
			
			//Function to calculate and output the orbit of a point in [0,1) given a multiple
			public static void itinerary(int num, int den, int tuple, int k) {
				double dnum=num, dden=den, dtuple=tuple, dm;		//creates doubles for decimal calculations
				int itin[]=new int[k];								//creates the array for storing the itinerary
				int g=0;											//counter to be used later
				int i=num*tuple;									//the next 10 lines are the same as in the orbit function
				for(i=i; i!=0; i*=tuple)
				{
					i=i%den;	
					dnum=i;
					if(i==num)
					{
						i=0;
					}
					else {
						for(int m=0; m<tuple; m++)					//calculate which part of the circle the orbit is based on tuple
						{
							dm=m;									//cycle through loop 1-tuple and update dm for double calculations
							if((dnum/dden)>=(dm/dtuple))			//calculate minimum part of the orbit
							{
								itin[g]=m;							//store largest m for which the inequality holds
							}
						}
						g++;										//update location in the array to take
					}
				}
				System.out.println("The itinerary of this orbit is: ");		//output of itinerary start
				for(g=0; g<k; g++)
				{
					System.out.println(itin[g]+" ");						//output of itinerary digits
				}
			}
			
			
			//Main
			public static void main(String[] args) {
				Scanner input = new Scanner(System.in);				//the next 11 lines are input
				int k=0;
				System.out.print("Enter an integer to multiply by at each iteration: ");
				int tuple = input.nextInt();
				System.out.println("Now enter an integer to be the numerator of your initial condition: ");
				int num = input.nextInt();
				System.out.println("Now input an integer to be the denominator of your initial condition: ");
				int den = input.nextInt();
				num=num%den;
				System.out.println("Your initial condition is: "+num+"/"+den);
				
				
				k=orbit(num, den, tuple);							//orbit calculation and output
				
				itinerary(num, den, tuple, k);						//itinerary calculation and output
				
				
				input.close();
			}
		}
