/*
 * problem06.java
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


public class problem06 {
    
    public static void main (String args[]) {

        double sum1 = 0, sum2 = 0, diff;

        for (double i = 1; i <= 100; i++) {
            sum1 += Math.pow(i, 2);
            sum2 += i;
        }

        sum2 = Math.pow(sum2, 2);
        diff = sum2 - sum1;
        System.out.println("Difference: " + diff);
    }
}

