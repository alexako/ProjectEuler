/*
 * problem02.java
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


public class problem02 {
    
    public static void main (String args[]) {

        Integer sum = 0;
        Integer num1 = 1, num2 = 2, temp;

        while (num2 < 4000000) {
            if (num2 % 2 == 0) {
                sum += num2;
            }
            temp = num2;
            num2 = num1 + num2;
            num1 = temp;
        }

        System.out.println("Sum: " + sum);
    }
}

