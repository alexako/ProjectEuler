/*
 * problem03.java
 * 
 * Copyright 2013 Alex <alex@kludge>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


public class problem03 {
    
    public static boolean isPrime(double num) {

        double limit = Math.sqrt(num) + 1;

        for (int i = 2; i < limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main (String args[]) {

        double target = 600851475143L;
        double limit = Math.sqrt(target) + 1;
        long max = 0;

        for (long i = 2; i < limit; i++) {
            if (target % i == 0 && isPrime(i)) {
                System.out.println("Factor: " + i);
                max = i;
            }
        }

        System.out.println("\nLargest: " + max);
    }
    
}

